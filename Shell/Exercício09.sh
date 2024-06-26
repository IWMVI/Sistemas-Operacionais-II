#!/bin/bash

if [$# -lt 1]; then
    echo: "Uso: $0 <argumento>"
    exit 1
fi

argumento="$1"

md5_hash=$(echo -n "$argumento" | md5sum | awk '{print $1}')

echo "MD5 do argumento '$argumento': $md5_hash"
