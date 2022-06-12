from pwn import *
from Crypto.Util.number import *


URL = "176.118.164.39"
PORT = 1337

r = remote(URL , PORT)

r.recvuntil(": ")
r.sendline("574923920397620")

r.recvuntil(": ")
r.sendline("212456")

r.recvuntil("N =  ")
N = int(r.recvline()[:-1])
print("N = ",N)
e = 65537

r.recvuntil(": ")
r.sendline("8564125")

M = [0 , 0]
while (M[0] + M[1]) % N == 0 :
    for i in range(2):
        r.recvuntil(": ")
        r.sendline("4")
        r.recvuntil(": ")
        r.sendline("4")
        M[i] = int(r.recvline()[:-1])

p = GCD(M[0] + M[1], N) # Самое главное в этом решении!!!

q = N // p
phi = (p - 1)*(q - 1)
d = inverse(e , phi)
print("p = ",p)
print("q = ",q)
print(p * q == N) 

r.recvuntil(": ")
r.sendline("0")
r.recvuntil(": ")
r.sendline("0")

r.recvuntil(": ")
r.sendline("1")
r.recvuntil("= ")

ct = int(r.recvline()[:-1])
password = pow(ct , d , N)
password = long_to_bytes(password)
print("Password = ", password)

r.recvuntil(": ")
r.sendline("2")
r.recvuntil(": ")
r.sendline(password)

flag = r.recvline()
print("FLAG: ", flag)
r.interactive()
