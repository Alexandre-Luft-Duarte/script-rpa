import time
import pyautogui
import pyperclip
from utils import ler_codigos_csv
from utils import verificar_e_clicar_primeira_opcao

pyautogui.PAUSE = 1
time.sleep(2)

# Definindo as coordenadas fixas para cada elemento da interface.
# Substitua os valores abaixo pelas coordenadas corretas do seu ambiente.
COORDENADAS = {
    'codigo_campo': (1116, 433),         
    'caixa_selecionar': (569, 553),                   
    'campo_de_consulta': (645, 366),     
    'codigo_campo_2': (1076, 448),
    'caixa_selecionar2': (564, 556),
}

def processar_codigo(codigo, primeira_vez=False):
    """
    Processa um único código de imóvel, executando a sequência de automação utilizando coordenadas fixas.
    :param codigo: Código do imóvel.
    """

    if not primeira_vez:
        # Copiar o código para a área de transferência
        pyperclip.copy(codigo)
        time.sleep(1)
        
        # Clicar no campo de código e colar o código
        pyautogui.click(COORDENADAS['campo_de_consulta'])
        pyautogui.click(COORDENADAS['codigo_campo_2'])
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyperclip.copy("")  # Limpar a área de transferência
        # Clicar na caixa de seleção
        pyautogui.click(COORDENADAS['caixa_selecionar2'])
        time.sleep(1)
        # Clicar na marcação do imóvel
        marcacao2 = pyautogui.locateCenterOnScreen('imagens/marcacao.png', confidence=0.8)
        pyautogui.click(marcacao2)
        # Copiar o código para a área de transferência
    else:
        pyperclip.copy(codigo)
        time.sleep(1)
        
        # Clicar no campo de código e colar o código
        pyautogui.click(COORDENADAS['codigo_campo'])
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyperclip.copy("")  # Limpar a área de transferência

        # Clicar na caixa de seleção
        pyautogui.click(COORDENADAS['caixa_selecionar'])
        time.sleep(1)
        
        # Clicar na marcação do imóvel
        marcacao = pyautogui.locateCenterOnScreen('imagens/marcacao.png', confidence=0.8)
        pyautogui.click(marcacao)


def main():
    """
    Função principal que inicia a automação.
    """
    time.sleep(2)  # Aguarda 2 segundos para preparar a interface
    caminho_csv = "arquivo/iptu_96_25032025.csv"
    codigos = ler_codigos_csv(caminho_csv)
    
    # Processa o primeiro código sem o clique extra
    if codigos:
        processar_codigo(codigos[0], primeira_vez=True)
    
    # Processa os demais com o clique adicional no campo de consulta
    for codigo in codigos[1:]:
        processar_codigo(codigo)

    
if __name__ == '__main__':
    main()
