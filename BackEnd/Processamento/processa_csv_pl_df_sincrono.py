import polars as pl
from time import time




if __name__ == "__main__":
    # file_path = r"Processamento\FIles\deletions\deletions.csv"
    fixed_path = r"Processamento\FIles\deletions\deletions_fixed.csv"

    # with open(file_path, "r", encoding="utf-8", errors="ignore") as f, \
    #     open(fixed_path, "w", encoding="utf-8") as out:

    #     buffer = ""
    #     for line in f:
    #         line = line.strip("\n").strip("\r")
    #         # verifica se a linha tem o número esperado de colunas (ex: 8)
    #         if buffer:
    #             buffer += " " + line
    #         else:
    #             buffer = line

    #         # se buffer tiver o número correto de separadores, salva
    #         if buffer.count(",") >= 7:  # ajusta de acordo com suas colunas
    #             out.write(buffer + "\n")
    #             buffer = ""

    df = pl.read_csv(
        fixed_path,
        quote_char='"'
    )

    print(df.shape)
