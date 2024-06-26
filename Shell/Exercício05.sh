#!/bin/bash

#Fazer backup do diretório /home/usuario para /tmp/ com o nome no formato backup_usuario_YYYY_MM_DD.tar.gz

diretorio_backup="/home/usuario"
diretorio_destino="/tmp"

backup_filename="backup_usuario_$(date + '%Y_%m_%d').tar.gz"

tar -czf "$diretorio_destino/$backup_filename" "$diretorio_backup"

echo "Backup de $diretorio_backup realizado em $diretorio_destino/$backup_filename"
