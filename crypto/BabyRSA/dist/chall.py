import os
from Crypto.Util.number import getPrime, inverse, bytes_to_long

key_size = 1024
p = getPrime(key_size // 2)
q = getPrime(key_size // 2)
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = inverse(e, phi)

with open("public_key.pem", "w") as pub_file:
    pub_file.write(f"{n}\n{e}")

with open("private_key.pem", "w") as priv_file:
    priv_file.write(f"{n}\n{d}")

with open("flag.txt", "rb") as f:
    m = f.read()

m_int = bytes_to_long(m)

c = pow(m_int, e, n)

print(f"Ciphertext: {c}")
