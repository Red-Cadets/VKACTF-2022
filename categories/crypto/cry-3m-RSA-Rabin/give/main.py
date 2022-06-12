#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from Crypto.Util.number import inverse,getPrime,bytes_to_long
from string import printable
import random


def keygen(bitsize):
    p = getPrime(bitsize)
    while p%4 != 3:
        p = getPrime(bitsize)
    return p

def Krit_Eiler(a,p):
    c = pow(a, (p-1) // 2 , p)
    if c == 1:
        return True
    return False

def check_input( phrase):
    while True:
        try:
            your_input = int(input(phrase))
            break
        except:
            print("Invalid int format")
    return your_input

with open("SuperSecretFlag.txt", "r") as f:
    flag = f.read()
with open("banner.txt","r") as f:
    banner = f.read()

password = b"".join(random.choice(printable[:62]).encode() for i in range(32))


bitsize = 1024
p = keygen(bitsize)
q = keygen(bitsize)

N = p * q
e = 65537
ct_pass = pow(bytes_to_long(password),e,N)
print(banner)



while True:
    print()
    print("[1] - Зашифрованный пароль")
    print("[2] - Ввести пароль")
    print("[0] - Exit")
    print()

    your_input = check_input("Выберите действие: ")
            
    if your_input == 1:
        print("Enc_password = ", ct_pass)
        
    elif your_input == 2:
        input_password = input("Введите пароль: ")

        if input_password.encode() == password:
            print(flag)
        else:
            print("Invalid password")

    elif your_input == 0:
        print("Exit . . .")
        exit()

    elif your_input == 574923920397620:
        print("Congratulations! Hope this helps you!")
        while True: 
            print()
            print("[....] - Публичный ключ")
            print("[....] - Калькулятор")
            print("[..0.] - Вернуться назад")
            print()  
            input_2 = check_input("Выберите действие: ")

            if input_2 == 212456:

                print("N = ",N)
                print("e = ", e)

            elif input_2 == 8564125:
                while True:
                    print()
                    print("[1] - Сложить 2 числа")
                    print("[2] - Вычитание 2 чисел")
                    print("[3] - Возвести в любую степень")
                    print("[4] - Извлечь квадратный корень")
                    print("[5] - Перемножить 2 числа")
                    print("[0] - Вернуться назад")
                    print()

                    input_calc = check_input("Выберите действие: ")

                    if input_calc == 1:
                        a = check_input("Введите число a: ")
                        b = check_input("Введите число b: ")
                        print("a + b = ", (a + b) % N)

                    elif input_calc == 2:
                        a = check_input("Введите число a: ")
                        b = check_input("Введите число b: ")
                        print("a - b = ", (a - b) % N)

                    elif input_calc == 3:
                        a = check_input("Введите число a: ")
                        b = check_input("Введите число b: ")
                        print("a ^ b = ", pow(a,b,N))
                    
                    elif input_calc == 4:
                        input_a = check_input("Введите число a: ")

                        if Krit_Eiler(input_a,p) == True and Krit_Eiler(input_a,q) == True:
                            M = []
                            a_p = pow(input_a , (p+1)//4 , p)
                            a_q = pow(input_a , (q+1)//4,  q)
                            M.append((a_p * q * inverse(q,p) + a_q * p * inverse(p,q)) % N)
                            M.append((-a_p * q * inverse(q,p) + a_q * p * inverse(p,q)) % N)
                            M.append((a_p * q * inverse(q,p) - a_q * p * inverse(p,q)) % N)
                            M.append((- a_p * q * inverse(q,p) - a_q * p * inverse(p,q)) % N)
                            print(random.choice(M))
                        else:
                            print("Invalid sqrt!")
                    
                    elif input_calc == 5:
                        a = check_input("Введите число a: ")
                        b = check_input("Введите число b: ")
                        print("a * b = ", (a * b) % N)
                    
                    elif input_calc == 0:
                        break
                    else:
                        print("Invalid option!")
            elif input_2 == 0:
                break
            else:
                print("Invalid option!")

    else:
        print("Invalid option!")
    

