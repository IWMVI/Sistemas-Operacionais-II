#!/bin/bash

#Localizar aquivos de texto que contêm a palavra "root" em /etc/* e salvar em roots.txt

diretorio="/etc"

roots_output="/home/usuario/roots.txt"

grep -r -l 'root' "$diretorio"/* >"$roots_output"

echo "Arquivos que contêm 'root' foram salvos em $roots_output"
