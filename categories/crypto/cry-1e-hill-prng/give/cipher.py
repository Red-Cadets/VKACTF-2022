from binascii import unhexlify
from random import randint
import numpy as np

class Stream_cipher():
    def __init__(self, M):
        self.A = np.matrix(M)
        self.N = 256
        self.x0 = [[randint(0,self.N)] for i in range(3)]

    def encrypt(self,pt):
        X0 = self.x0
        gamma = []
        lenght = len(pt) + 3 - len(pt) % 3
        for i in range(0,lenght,3):
            X = self.A * X0 % 256
            X0 = X
            gamma.extend(list(X))
        ct = ""
        for i in range(len(pt)):
            ct += hex(int(gamma[i]) ^ int(pt[i]))[2:].rjust(2,"0")
        return unhexlify(ct)

    def decrypt(self,ct):
        return self.encrypt(ct)
    
M = ?

f = open("secret_data.db" , "rb")
data = f.read()
f.close()

cipher = Stream_cipher(M)
enc_flag = cipher.encrypt(data)

f1 = open("secret_data.enc","wb")
f1.write(enc_flag)
f1.close()
