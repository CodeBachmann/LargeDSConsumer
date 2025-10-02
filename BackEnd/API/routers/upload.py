from fastapi import FastAPI, UploadFile, File, Depends, HTTPException, APIRouter
import polars as pl
from typing import Generator
from database import get_db

from time import time
router = APIRouter(prefix="/uploads", tags=["Uploads"])

@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...), db=Depends(get_db)):
    collection = db["dataset_1"]

    try:
        # LazyFrame para streaming
        lazy_df = pl.scan_csv(file.file)

        # Processar em batches
        for batch in lazy_df.collect(streaming=True).iter_slices(100_000):
            # Garantir que é DataFrame
            if isinstance(batch, pl.Series):
                batch = batch.to_frame()

            # Converter -1/1 para 0/1
            batch = batch.with_columns([
                ((pl.col(col) + 1) // 2).alias(col)
                for col in batch.columns if col != "image_id"
            ])

            # Inserir no MongoDB
            records = batch.to_dicts()
            if records:
                collection.insert_many(records)

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

    return {"filename": file.filename, "status": "uploaded"}