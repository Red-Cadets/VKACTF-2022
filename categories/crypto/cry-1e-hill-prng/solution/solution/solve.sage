from binascii import unhexlify
import numpy as np

def recovery_Matr(gamma):
    N = 256
    assert len(gamma) == 12
    Matr = Matrix(Zmod(N) , [gamma[:3],gamma[3:6],gamma[6:9]])
    A = []
    for i in range(3):
        b = [gamma[ 3 + i ] , gamma[6 + i] , gamma[9 + i] ]
        b = vector(Zmod(N) , b)
        try:
            a = Matr.solve_right(b)
            A.append(a)
        except:
            continue
    A_ = Matrix(Zmod(N) , A)
    X0 = vector(Zmod(N) , gamma[:3])
    seed = (A_ ^ (-1)) * X0
    return A , seed

class Stream_cipher():
    def __init__(self, M,seed):
        self.A = np.matrix(M)
        self.N = 256
        self.x0 = [[int(i)] for i in seed]

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
            ct += hex(int(gamma[i]) ^^ int(pt[i]))[2:].rjust(2,"0")
        return unhexlify(ct)

    def decrypt(self,ct):
        return self.encrypt(ct)


f = open("secret_data.enc","rb")
enc_data = f.read()

standard_byte = unhexlify("53514C69746520666F726D6174203300") # Первые фиксированные 16 байт в заголовке db файлов
gamma = []
for i,j in zip(standard_byte[:12],enc_data[:12]):
    gamma.append(int(i) ^^ int(j))
print(gamma)


A , seed = recovery_Matr(gamma)
cipher = Stream_cipher(A, seed)
flag = cipher.decrypt(enc_data)
f1 = open("secret_data.db","wb")
f1.write(flag)
f1.close()
