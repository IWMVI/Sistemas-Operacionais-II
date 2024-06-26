#!/bin/bash

#Abrir, com script BASH ou PYTHON, o arquivo contendo usuários do sistema
#(entende-se que se saiba qual arquivo é). Linha por linha procurar usuários que possuam como
#shell algum path diferente de /bin/bash e /usr/sbin/nologin. Caso seja diferente, imprima na
#tela o usuário e o path do shell.

arquivo_usuarios="/etc/passwd"

while IFS=: read -r username x userid groupid gecos homedir shell; do
    if [["$shell" != "/bin/bash" && "$shell" != "/usr/sbin/nologin"]]; then
        echo "Usuário: $username - Shell: $shell"
    fi
done <"$arquivo_usuarios"
