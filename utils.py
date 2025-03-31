import csv
import os
import time
import pyautogui

def ler_codigos_csv(caminho_csv):
    """
    Lê um arquivo CSV e retorna uma lista com os códigos dos imóveis.
    :param caminho_csv: Caminho para o arquivo CSV.
    :return: Lista de códigos.
    """
    codigos = []
    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_csv}")
    with open(caminho_csv, "r") as arquivo:
        reader = csv.DictReader(arquivo, delimiter=';')
        for row in reader:
            codigos.append(row['imovel_prefeitura'])
    return codigos

def localizar_imagem(imagem, tentativas=5, intervalo=1, confidence=0.8):
    """
    Tenta localizar uma imagem na tela várias vezes, aguardando um intervalo entre as tentativas.
    :param imagem: Caminho da imagem para localizar.
    :param tentativas: Número máximo de tentativas.
    :param intervalo: Tempo de espera entre as tentativas (em segundos).
    :param confidence: Nível de confiança para a localização.
    :return: Posição central da imagem se encontrada, ou None.
    """
    for _ in range(tentativas):
        posicao = pyautogui.locateCenterOnScreen(imagem, confidence=confidence)
        if posicao:
            return posicao
        time.sleep(intervalo)
    return None
