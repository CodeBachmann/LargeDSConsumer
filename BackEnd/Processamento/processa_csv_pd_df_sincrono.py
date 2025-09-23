import pandas as pd
from math import floor
from time import time


class Reader:
    def __init__(self):
        self.bad_lines = []

    def save_bad_lines(self, bad_line):   # note the 'self' param
        self.bad_lines.append(bad_line)
        return None


    def count_csv_rows(self, file_path):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)

    def chunk_file_reader(self, file_path, proc_print, chunk_size, columns=[]):
        df = pd.read_csv(file_path, skiprows=1, nrows=100)
        if len(columns) == 0:
            columns = [f"Column_{i+1}" for i in range(len(df.columns))]
        loop_count = 1
        final_size = self.count_csv_rows(file_path)
        bar_algorithm = 100/final_size
        start = time()

        for chunk in pd.read_csv(file_path, chunksize=chunk_size, on_bad_lines="warn"):
            if loop_count % proc_print == 0:
                act = floor(loop_count * chunk_size * bar_algorithm)
                print(f"Actual file process: {act}%")
            loop_count += 1

        end = time()
        delta = end - start
        rows_p_sec = floor(final_size/delta)
        print(f"Total Rows: {final_size}\nTime: {delta}\n Rows p/ Second: {rows_p_sec}")


if __name__ == "__main__":
    r = Reader()
    #file_path = r"Processamento\Files\deletions\deletions.csv"
    file_path = r"C:\Users\adm\Desktop\DataSets\customers-2000000.csv"

    columns = [
    "creation_timestamp (tempo de época Unix em milissegundos)",
    "criador",
    "deletion_timestamp (tempo de época Unix em milissegundos)",
    "excluidor",
    "assunto (MID)",
    "predicado (MID)",
    "objeto (MID/literal)",
    "language_code"]

    r.chunk_file_reader(file_path=file_path, proc_print=10, chunk_size=40000, columns=columns)

