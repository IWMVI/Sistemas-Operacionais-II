#!/bin/bash

#Calcular o MD5 para cada arquivo listado em arquivos.txt e salvar em md5.txt

arquivos_input="/home/usuario/arquivos.txt"
md5_output="/home/usuario/md5.txt"

>"$md5_output"

while IFS= read -r filepath; do
    md5=$(md5sum "$filepath" | awk '{print $1}')
    echo "$filepath;$md5" >>"$md5_output"
done <"$arquivos_input"

echo "Hashes MD5 dos aquivos foram salvos em $md5_output"
