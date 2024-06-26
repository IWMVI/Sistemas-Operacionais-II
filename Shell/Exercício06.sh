#!/bin/bash

# Fazer um scrpit com uma função recebendo como parâmetro o nome de um pacote. Verificar se o pacote existe para a instalação
# no apt, ppa na nuvem
# apt.cache show

if [ "$(id -u)" -ne 0]; then
    echo "Este script precisa ser executado como root."
    exit 1
fi

verificar_pacote() {
    local pacote ="$1"
    echo "Verificando pacote: $pacote"

    if apt-cache show "$pacote" >/dev/null 2>&1; then
        echo "Pacote '$pacote' encontrado no apt."
        return 0
    fi

    ppa="ppa:exemplo/ppa"
    if apt-cache show "$pacote" | grep -q "$ppa"; then
        echo "Pacote '$pacote' encontrado no PPA: $ppa."
    fi

    if curl -sSL "https://exemplo.com/pacotes/$pacote" | grep -q "disponível"; then
        echo "Pacote '$pacote' encontrado na nuvem."
        return 0
    fi

    echo "Pacote '$pacote' não encontrado para instalação."
    return 1
}

if verificar_pacote "$1"; then
    echo "Pode proceder com a instalação do pacote '$1'."
else
    echo "Pacote '$1' não está disponível para instalação"
fi
