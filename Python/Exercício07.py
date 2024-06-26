#!/usr/bin/env python3

import sys

def verificar_shells(arquivo_usuarios):
    try:
        with open(arquivo_usuarios, 'r') as f:
            for linha in f:
                campos = linha.strip().split(':')
                if len(campos) >= 7:
                    username = campos [0]
                    shell = campos[-1]
                    if shell != '/bin/bash' and shell != '/usr/sbin/nologin':
                        print(f"Usuário: {username} - Shell: {shell}")
    except FileNotFoundError:
        print(f"Arquivo {arquivo_usuarios} não encontrado.")
        sys.exit(1)
    except PermissionError:
        print(f"Erro: Permissão negada para acessar {arquivo_usuarios}.")
        sys.exit(1)

arquivo_usuarios = '/etc/passwd'

verificar_shells(arquivo_usuarios)