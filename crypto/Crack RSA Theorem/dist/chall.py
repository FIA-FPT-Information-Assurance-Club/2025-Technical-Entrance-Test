from Crypto.Util.number import getPrime, bytes_to_long
from random import randbytes

flag = b'FIA{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}' + randbytes(100) # some random bytes to make the flag longer
m = bytes_to_long(flag)
e = 3 # should be ok, right?

# 3 times a charm
for i in range(3):
    n = getPrime(1024) * getPrime(1024) # different n for you every time hehe
    c = pow(m, e, n)

    print(f'n{i} = {n}')
    print(f'c{i} = {c}')
    print()