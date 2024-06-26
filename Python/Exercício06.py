#!/usr/bin/env python3
import os
import sys
import subprocess

# Função para verificar se o usuário é root
def verificar_root():
    return os.geteuid() == 0

# Função para verificar a existência do pacote
def verificar_pacote(pacote):
    print(f"Verificando pacote: {pacote}")

    # Verifica no apt
    try:
        subprocess.check_call(["apt-cache", "show", pacote])
        print(f"Pacote '{pacote}' encontrado no apt.")
        return True
    except subprocess.CalledProcessError:
        pass

    # Verifica em PPA (exemplo de PPA)
    ppa = "ppa:exemplo/ppa"
    try:
        output = subprocess.check_output(["apt-cache", "show", pacote]).decode("utf-8")
        if ppa in output:
            print(f"Pacote '{pacote}' encontrado no PPA: {ppa}.")
            return True
    except subprocess.CalledProcessError:
        pass

    # Verifica na nuvem (exemplo de nuvem)
    try:
        response = subprocess.check_output(["curl", "-sSL", f"https://exemplo.com/pacotes/{pacote}"]).decode("utf-8")
        if "disponível" in response:
            print(f"Pacote '{pacote}' encontrado na nuvem.")
            return True
    except subprocess.CalledProcessError:
        pass

    # Se não encontrado em nenhum lugar
    print(f"Pacote '{pacote}' não encontrado para instalação.")
    return False

# Verifica se o usuário é root antes de prosseguir
if not verificar_root():
    print("Este script precisa ser executado como root.")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Uso: ./verificar_pacote.py <nome_pacote>")
    sys.exit(1)

nome_pacote = sys.argv[1]
if verificar_pacote(nome_pacote):
    print(f"Pode proceder com a instalação do pacote '{nome_pacote}'.")
else:
    print(f"Pacote '{nome_pacote}' não está disponível para instalação.")
