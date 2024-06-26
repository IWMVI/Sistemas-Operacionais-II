#!/bin/bash

#Listar MAC ADDRESS das interfaces de rede e salvar em macs.txt

macs_output="/home/usuario/macs.txt"

ifconfig -a | grep -oE '([0-9a-fA-F]{2}:){5}[0-9a-fA-F{2}]' >"$macs_output"

echo "MAC ADDRESS das interfaces de rede foram salvos em $macs_output"
