import pyautogui
import time
import csv
import pyperclip

time.sleep(2)
pyautogui.PAUSE = 1

codes = list()  # Cria uma lista para colocar os códigos dos imóveis
with open("arquivo/iptu_96_25032025.csv", "r") as arquivo:
    reader = csv.DictReader(arquivo, delimiter=';')
    for row in reader:
        codes.append(row['imovel_prefeitura'])

for i in codes:
    print(f"Processando código: {i}")
    pyperclip.copy(i)
    time.sleep(1)

    try:
        posicao_campo = pyautogui.locateCenterOnScreen('imagens/codigo_campo.png', confidence=0.8)
        print(f"Posição do campo encontrada: {posicao_campo}")
    except pyautogui.ImageNotFoundException:
        posicao_campo = None
        print("Imagem 'codigo_campo.png' não encontrada.")

    if posicao_campo:
        pyautogui.click(posicao_campo)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyperclip.copy("")
        pyautogui.click('imagens/caixa_selecionar.png', confidence=0.8)
        time.sleep(1)
        posicao_marcacao = pyautogui.locateCenterOnScreen('imagens/marcacao.png', confidence=0.8)
        print(f"Posição da marcação encontrada: {posicao_marcacao}")
        if posicao_marcacao:
            pyautogui.click(posicao_marcacao)
            pyautogui.click('imagens/emissao.png', confidence=0.8)
            pyautogui.hotkey('ctrl', 's')
            pyautogui.press('enter')
        else:
            print("Imagem 'marcacao.png' não encontrada.")
    else:
        try:
            posicao_consulta = pyautogui.locateCenterOnScreen('imagens/campo_de_consulta.png', confidence=0.8)
            print(f"Posição do campo de consulta encontrada: {posicao_consulta}")
        except pyautogui.ImageNotFoundException:
            posicao_consulta = None
            print("Imagem 'campo_de_consulta.png' não encontrada.")

        if posicao_consulta:
            pyautogui.click(posicao_consulta)
            time.sleep(1)
            posicao_campo_2 = pyautogui.locateCenterOnScreen('imagens/codigo_campo_2.png', confidence=0.8)
            print(f"Posição do campo de código (2) encontrada: {posicao_campo_2}")
            if posicao_campo_2:
                pyautogui.doubleClick(posicao_campo_2)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('delete')
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                pyperclip.copy("")
                pyautogui.click('imagens/caixa_selecionar.png', confidence=0.8)
                time.sleep(1)
            else:
                print("Imagem 'codigo_campo_2.png' não encontrada.")
        else:
            print("Nenhuma imagem de campo encontrada para esse código.")
