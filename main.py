import time
import pyautogui
import pyperclip
from utils import ler_codigos_csv
from utils import verificar_e_clicar_primeira_opcao
from utils import sem_iptu


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
    'campo_de_consulta2': (705, 416),
}

def processar_codigo(codigo, primeira_vez=False):
    """
    Processa um único código de imóvel, executando a sequência de automação utilizando coordenadas fixas.
    Se a mensagem "sem IPTU" for detectada, o fluxo para esse imóvel é interrompido (usando return).
    :param codigo: Código do imóvel.
    """
    if not primeira_vez:
        pyperclip.copy(codigo)
        time.sleep(1)
        
        # Clicar no campo de consulta e no campo de código alternativo
        pyautogui.click(COORDENADAS['campo_de_consulta'])
        pyautogui.click(COORDENADAS['codigo_campo_2'])

        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyperclip.copy("")  # Limpar a área de transferência

        # Verifica se a mensagem "sem IPTU" apareceu; se sim, pula esse imóvel.
        if sem_iptu(confidence=0.9, timeout=3, region=(880, 356, 450, 50)):
            print('Sem IPTU. Pulando imóvel!')
            return  # Interrompe a função para esse imóvel
        
        # Continuar com os demais comandos se IPTU estiver presente
        pyautogui.click(COORDENADAS['caixa_selecionar2'])
        time.sleep(1)

        verificar_e_clicar_primeira_opcao(confidence=0.9, timeout=3)

        try:
            marcacao2 = pyautogui.locateCenterOnScreen('imagens/marcar_todas.png', confidence=0.8)
            pyautogui.click(marcacao2)
        except pyautogui.ImageNotFoundException:
            print("Imagem de marcação não encontrada. Pulando imóvel!")
            return

    else:
        pyperclip.copy(codigo)
        time.sleep(1)
        
        # Clicar no campo de código e colar o código
        pyautogui.click(COORDENADAS['codigo_campo'])
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyperclip.copy("")  # Limpar a área de transferência

        if sem_iptu(confidence=0.9, timeout=3, region=(880, 356, 450, 50)):
            print('Sem IPTU. Pulando imóvel!')
            return
     
        pyautogui.click(COORDENADAS['caixa_selecionar'])
        time.sleep(1)
        
        verificar_e_clicar_primeira_opcao(confidence=0.9, timeout=3)

        try:
            marcacao = pyautogui.locateCenterOnScreen('imagens/marcar_todas.png', confidence=0.8)
            pyautogui.click(marcacao)
        except pyautogui.ImageNotFoundException:
            print("Imagem de marcação não encontrada. Pulando imóvel!")
            return

        #pyautogui.click(x=1161, y=896)
 
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
