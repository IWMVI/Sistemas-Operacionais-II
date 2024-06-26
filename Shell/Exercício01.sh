#!/bin/bash

#Script que procura todos os arquivos do tipo especial de bloco.

diretorio = "/"

arquivo_saida = "/home/usuario/dispositivos.txt"

find "$diretorio" -type b >"$arquivo_saida"

echo "Caminhos dos arquivos especiais de bloco foram salvos em $arquivo_saida"
