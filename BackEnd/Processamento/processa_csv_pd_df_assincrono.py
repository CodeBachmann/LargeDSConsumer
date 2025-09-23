import pandas as pd
from math import floor
from time import time
from concurrent.futures import ProcessPoolExecutor, as_completed


class AssyncReader:

    def read_chunk(file_path, skiprows, nrows, columns):
        df = pd.read_csv(
            file_path,
            skiprows=skiprows,
            nrows=nrows,
            header=None,
            on_bad_lines="warn"
        )
        df.columns = columns
        return df

    def count_rows(self, file_path):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)

    def chunk_file_reader(self, file_path, chunk_size):
        df = pd.read_csv(file_path, nrows=100)
        columns = [f"Column_{i+1}" for i in range(len(df.columns))]
        final_size = self.count_rows(file_path)
        start = time()
        offsets = range(1, final_size, chunk_size)
        dfs = []

        with ProcessPoolExecutor(max_workers=10) as executor:
            futures = [
                executor.submit(AssyncReader.read_chunk, file_path, skip, chunk_size, columns)
                for skip in offsets
            ]
            for future in as_completed(futures):
                dfs.append(future.result())
            
        
        end = time()
        delta = end - start
        rows_p_sec = floor(final_size/delta)
        print(f"Total Rows: {final_size}\nTime: {delta}\n Rows p/ Second: {rows_p_sec}")


if __name__ == "__main__":
    ar = AssyncReader()
    #file_path = r"Processamento\Files\deletions\deletions.csv"
    file_path = r"C:\Users\adm\Desktop\DataSets\customers-2000000.csv"

    ar.chunk_file_reader(file_path=file_path, chunk_size=40000)

