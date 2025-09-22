import pandas as pd
from math import floor
from time import time
from concurrent.futures import ProcessPoolExecutor


class AssyncReader:

    def count_rows(file_path):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)

    def chunk_file_reader(self, file_path, chunk_size):
        df = pd.read_csv(file_path, nrows=100)
        columns = [f"Column_{i+1}" for i in range(len(df.columns))]
        final_size = self.count_rows(file_path)
        start = time()

        for chunk in pd.read_csv(file_path, chunksize=chunk_size, on_bad_lines="warn"):
            chunk.columns = columns

        end = time()
        delta = end - start
        rows_p_sec = floor(final_size/delta)
        print(f"Total Rows: {final_size}\nTime: {delta}\n Rows p/ Second: {rows_p_sec}")


if __name__ == "__main__":
    ar = AssyncReader()
    file_path = r"Processamento\FIles\deletions\deletions.csv"
    ar.chunk_file_reader(file_path=file_path, proc_print=10, chunk_size=40000)

