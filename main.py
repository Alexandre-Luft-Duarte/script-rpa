import time
import pyautogui
import pyperclip
from teste import ler_codigos_csv, localizar_imagem

pyautogui.PAUSE = 1

def processar_codigo(codigo):
    """
    Processa um único código de imóvel, executando a sequência de automação necessária.
    :param codigo: Código do imóvel.
    """
    pyperclip.copy(codigo)
    time.sleep(1)
    
    posicao_campo = localizar_imagem('imagens/codigo_campo.png', confidence=0.8)
    if posicao_campo:
        pyautogui.click(posicao_campo)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyperclip.copy("")
        pyautogui.click('imagens/caixa_selecionar.png', confidence=0.8)
        time.sleep(1)
        posicao_marcacao = localizar_imagem('imagens/marcacao.png', confidence=0.8)
        if posicao_marcacao:
            pyautogui.click(posicao_marcacao)
            pyautogui.click('imagens/emissao.png')
            time.sleep(7)
            pyautogui.click('imagens/baixar.png')
    else:
        posicao_consulta = localizar_imagem('imagens/campo_de_consulta.png', confidence=0.8)
        if posicao_consulta:
            pyautogui.click(posicao_consulta)
            time.sleep(1)
            posicao_campo_2 = localizar_imagem('imagens/codigo_campo_2.png', confidence=0.8)
            if posicao_campo_2:
                pyautogui.doubleClick(posicao_campo_2)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('delete')
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                pyperclip.copy("")
                pyautogui.click('imagens/caixa_selecionar.png', confidence=0.8)
                time.sleep(1)

def main():
    """
    Função principal que inicia a automação.
    """
    time.sleep(2)  # Aguarda 2 segundos para preparar a interface
    caminho_csv = "arquivo/iptu_96_25032025.csv"
    codigos = ler_codigos_csv(caminho_csv)
    
    for codigo in codigos:
        processar_codigo(codigo)
    
if __name__ == '__main__':
    main()
