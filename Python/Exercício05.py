# Importa o módulo datetime para lidar com datas e horas
import datetime
# Importa o módulo os para interagir com o sistema operacional
import os
# Importa o módulo tarfile para criar arquivos tar.gz
import tarfile

# Define uma função para fazer backup de um diretório e salvar em outro
def fazer_backup(diretorio_origem, diretorio_destino):
    # Obtém a data atual no formato 'YYYY_MM_DD'
    data_hoje = datetime.datetime.now().strftime('%Y_%m_%d')
    # Define o nome do arquivo de backup usando a data atual
    nome_backup = f'backup_usuario_{data_hoje}.tar.gz'
    # Define o caminho completo onde o arquivo de backup será salvo
    caminho_backup = os.path.join(diretorio_destino, nome_backup)

    # Abre um arquivo tar.gz em modo de escrita ('w:gz')
    with tarfile.open(caminho_backup, 'w:gz') as tar:
        # Adiciona o diretório de origem ao arquivo tar.gz com o nome base do diretório
        tar.add(diretorio_origem, arcname=os.path.basename(diretorio_origem))

# Define o diretório de origem que será feito backup
diretorio_origem = '/home/usuario'
# Define o diretório de destino onde o arquivo de backup será salvo
diretorio_destino = '/tmp'

# Chama a função para fazer backup do diretório de origem para o diretório de destino
fazer_backup(diretorio_origem, diretorio_destino)
