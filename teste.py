import pyautogui
import time
import csv
import pyperclip
import shutil
import os

time.sleep(2)
pyautogui.PAUSE = 1

codes = list() #cria uma lista para colocar os códigos dos imóveis
with open("arquivo/iptu_96_25032025.csv", "r") as arquivo: # abre um arquivo csv
    reader = csv.DictReader(arquivo, delimiter=';') #le o arquivo e delimita a divisão das colunas pelo ";"
    for row in reader: #le os elementos do arquivo
        codes.append(row['imovel_prefeitura']) #insere na lista os códigos dos imóveis


for i in codes: #percorre a lista código por código
    pyperclip.copy(i) #copia o código na posição i(que vai mudando conforme entra no loop)
    time.sleep(1)

    try:
        posicao_campo = pyautogui.locateCenterOnScreen('imagens/codigo_campo.png', confidence=0.8) #procura pela imagem que insere os códigos
    except pyautogui.ImageNotFoundException:
        posicao_campo = None

    if posicao_campo:
        pyautogui.click(posicao_campo)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyperclip.copy("")
        pyautogui.click('imagens/caixa_selecionar.png')
        time.sleep(1)
        posicao_marcacao = pyautogui.locateCenterOnScreen('imagens/marcacao.png', confidence=0.8)
        if posicao_marcacao:
            pyautogui.click(posicao_marcacao)
            pyautogui.click('imagens/emissao.png')
            pyautogui.hotkey('ctrl', 's')
            pyautogui.press('enter')
    else:
        try:
            posicao_consulta = pyautogui.locateCenterOnScreen('imagens/campo_de_consulta.png', confidence=0.8)
        except pyautogui.ImageNotFoundException:
            posicao_consulta = None
    
        if posicao_consulta:
            pyautogui.click(posicao_consulta)
            time.sleep(1)
            posicao_campo_2 = pyautogui.locateCenterOnScreen('imagens/codigo_campo_2.png', confidence=0.8)
            if posicao_campo_2:
                pyautogui.doubleClick(posicao_campo_2)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('delete')
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                pyperclip.copy("")
                pyautogui.click('imagens/caixa_selecionar.png')
                time.sleep(1)
                posicao_marcacao = pyautogui.locateCenterOnScreen('imagens/marcacao.png', confidence=0.8)
                if posicao_marcacao:
                    pyautogui.click(posicao_marcacao)
                    pyautogui.click('imagens/emissao.png')
                    time.sleep(3)
                    pyautogui.hotkey('ctrl', 's')
                    pyautogui.press('enter')
                    campo_origem = '/Downloads/teste.pdf'
                    pasta_pdfs = ivan
                    hhhnjunjnjnhnhbhbgybb
      