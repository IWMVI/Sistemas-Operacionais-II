# Importa o módulo os para interagir com o sistema operacional
import os

# Define uma função para localizar arquivos de texto que contenham uma palavra específica e salvar os resultados em um arquivo
def localizar_arquivos_com_palavra(root_dir, palavra, arquivo_saida):
    # Abre o arquivo de saída especificado em 'arquivo_saida' para escrita ('w')
    with open(arquivo_saida, 'w') as f:
        # Percorre recursivamente todos os diretórios a partir de 'root_dir'
        for root, _, files in os.walk(root_dir):
            # Itera sobre cada arquivo encontrado nos diretórios
            for filename in files:
                # Cria o caminho completo para o arquivo atual
                filepath = os.path.join(root, filename)
                # Verifica se o caminho é de um arquivo e se o nome termina com '.txt'
                if os.path.isfile(filepath) and filename.endswith('.txt'):
                    # Abre o arquivo atual em modo de leitura ('r')
                    with open(filepath, 'r') as file:
                        # Verifica se a palavra procurada está em alguma linha do arquivo
                        if any(palavra in line for line in file):
                            # Escreve o caminho do arquivo no arquivo de saída, seguido por uma nova linha
                            f.write(filepath + '\n')

# Diretório base onde a busca será realizada
diretorio_base = '/etc/'
# Palavra que será procurada nos arquivos de texto
palavra_procurada = 'root'
# Caminho do arquivo onde os resultados serão salvos
arquivo_saida = '/home/usuario/roots.txt'

# Chama a função para localizar arquivos com a palavra 'root' no diretório base e salvar os resultados no arquivo de saída
localizar_arquivos_com_palavra(diretorio_base, palavra_procurada, arquivo_saida)
