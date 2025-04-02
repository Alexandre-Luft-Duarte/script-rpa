import csv
import os

def ler_codigos_csv(caminho_csv):
    """
    Lê um arquivo CSV e retorna uma lista com os códigos dos imóveis.
    :param caminho_csv: Caminho para o arquivo CSV.
    :return: Lista de códigos.
    """
    codigos = []
    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_csv}")
    with open(caminho_csv, "r", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo, delimiter=';')
        for row in reader:
            codigos.append(row['imovel_prefeitura'])
    return codigos
