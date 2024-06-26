import os
import hashlib

if len(sys.argv) < 2:
    print("Uso: Python script.py <argumento>")
    sys.exit(1)

argumento = sys.argv[1]

md5_hash = hashlib.md5(argumento.encode()).hexdigest()

print(f"MD5 do argumento '{argumento}':{md5_hash}")
