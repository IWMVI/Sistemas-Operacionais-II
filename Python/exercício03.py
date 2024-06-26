# Importa o módulo subprocess para executar comandos externos
import subprocess


# Define uma função para listar o MAC ADDRESS das interfaces de rede e salvar em um arquivo
def listar_mac_address(arquivo_saida):
    # Executa o comando 'ifconfig' e captura a saída padrão usando subprocess.run
    resultado = subprocess.run([''], stdout=subprocess.PIPE, text=True)

    # Abre o arquivo de saída especificado em 'arquivo_saida' para escrita ('w')
    with open(arquivo_saida, 'w') as f:
        # Escreve a saída do comando '' no arquivo de saída
        f.write(resultado.stdout)


# Caminho do arquivo onde os MAC ADDRESS serão salvos
arquivo_saida = '/home/usuario/macs.txt'

# Chama a função para listar os MAC ADDRESS das interfaces de rede e salvar no arquivo de saída
listar_mac_address(arquivo_saida)
