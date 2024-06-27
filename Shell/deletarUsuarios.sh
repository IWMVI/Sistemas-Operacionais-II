#!/bin/bash

# Verifica se o script está sendo executado como root
if [ "$EUID" -ne 0 ]; then
    echo "Este script precisa ser executado como root."
    exit 1
fi

# Passo 1: Remover todos os usuários do grupo
members=$(getent group alunos | cut -d: -f4)

if [ -z "$members" ]; then
    echo "O grupo alunos não possui usuários."
else
    echo "Removendo usuários do grupo alunos..."
    for member in $members; do
        deluser $member alunos
        if [ $? -eq 0 ]; then
            echo "Usuário $member removido do grupo alunos."
        else
            echo "Erro ao remover usuário $member do grupo alunos."
        fi
    done
fi

# Passo 2: Remover o grupo alunos
echo "Removendo o grupo alunos..."
groupdel alunos

if [ $? -eq 0 ]; then
    echo "Grupo alunos removido com sucesso."
else
    echo "Erro ao remover o grupo alunos."
fi
