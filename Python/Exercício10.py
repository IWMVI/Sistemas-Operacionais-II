#!/usr/bin/python3

#Fazer um script em Python que execute um novo processo (ls -l /), pegue o output e coloque em uma variável.

import subprocess

comando = ['ls', '-l', '/']

resultado = subprocess.run(comando, capture_output=True ,text=True)

saida = resultado.stdout

print(saida)