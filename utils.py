import csv
import os
import pyautogui
import time

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


def verificar_e_clicar_primeira_opcao(confidence=0.8, timeout=3):
    """
    Verifica se a imagem da primeira opção de parcelamento ('imagens/primeira_opcao.png')
    está presente na tela. Se encontrada, clica nela e retorna True; caso contrário, retorna False.
    """
    inicio = time.time()
    while time.time() - inicio < timeout:
        posicao = pyautogui.locateCenterOnScreen('imagens/imagem_parcelas.png', confidence=confidence)
        if posicao:
            pyautogui.click(posicao)
            time.sleep(1)
            return True
        time.sleep(0.5)
    return False