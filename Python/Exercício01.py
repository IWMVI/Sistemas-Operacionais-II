# Importa o módulo "os" para utilizar funcionalidades de interação com o sistema operacional
import os

# Define uma função que procura arquivos do tipo especial de bloco em um diretório e os lista em um arquivo de saída
def procurar_aquirvos_especiais_bloco(diretorio, arquivo_saida):
    # Abre o arquivo especificado em "arquivo_saida" para escrita ('w'), usando 'f' como alias
    with open(arquivo_saida, 'w') as f:
        # Percorre recursivamente todos os diretórios a partir de 'diretorio'
        for root, _, files in os.walk(diretorio):
            # Itera sobre cada arquivo encontrado nos diretórios
            for filename in files:
                # Cria o caminho completo para o arquivo atual
                filepath = os.path.join(root, filename)
                # Verifica se o arquivo é do tipo especial de bloco
                if os.path.isfile():
                    # Escreve o caminho do arquivo no arquivo de saída, seguido por uma nova linha
                    f.write(filepath + '\n')

# Diretório base de onde a busca será iniciada
diretorio_base = '/'

# Arquivo onde os caminhos dos arquivos do tipo especial de bloco serão salvos
arquivo_saida = '/home/usuario/dispositivos.txt'

# Chama a função para procurar arquivos do tipo especial de bloco no diretório base e salvar os resultados no arquivo de saída
procurar_aquirvos_especiais_bloco(diretorio_base, arquivo_saida)
