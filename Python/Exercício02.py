#Calcular MD5 de arquivos listados em um arquivo e salvar em outro

#Importa o módulo para calcular o MD5 dos arquivos.
import hashlib

#Define uma função para calcular o MD5
def calcular_md5_arquivos(arquivo_entrada, aquivo_saida):
    #Abre o aquivo de entrada para leitura ('r') e o arquivo de saída par escrita ('w')
    with open(arquivo_entrada, 'r') as f_in, open(arquivo_saida, 'w') as f_out:
        #Itera sobre cada linha do aquivo de entrada
        for linha in f_in:
            #Remove espaços em branco e caracteres de nova linha da linha atual
            arquivo = linha.strip()
            try:
                #Abre o arquivo atual em modo de leitura binária ('rb')
                with open(arquivo, 'rb') as file:
                    #Inicializa um objeto de hash MD5
                    hash_md5 = hashlib.md5()
                    #Lê o arquivo em blocos de 4096 bytes e atualiza o hash MD5 com cada bloco lido
                    for chunk in iter(lambda: file.read(4096), b""):
                        hash_md5.update(chunk)
                        #Obtém o valor do hash MD5 em formato hexadecimal
                    md5 = hash_md5.hexdigest()
                    #Escreve no arquivo de saída o caminho do arquivo e seu respectivo MD5, seprando-os por ';'
                    f_out.write(f'{arquivo};{md5}\n')
            except FileNotFoundError:
                #Se o arquivo não for encontrado exibe uma mensagem de erro
                print (f'Aquivo não encontrado: {arquivo}')

#Caminho que contém os caminhos dos arquivos cujo MD5 será calculado
arquivo_entrada = '/home/usuario/arquivos.txt'

#Caminho do arquivo onde os resultados do cálculo de MD5 serão salvos
arquivo_saida = '/home/usuario/md5.txt'

#Chamada da função.
calcular_md5_arquivos(arquivo_entrada, arquivo_saida)