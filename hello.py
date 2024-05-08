import string
import random
import time
import os

lista = list(string.printable)

for i in range(5):
    lista.pop(-1)

msg = ""
while msg != "Hello World":
    letra = random.choice(lista)
    print(msg + letra)
    if letra == "H" and msg == "":
        msg = msg + letra
    elif letra == "e" and msg == "H":
        msg = msg + letra
    elif letra == "l" and msg == "He":
        msg = msg + letra
    elif letra == "l" and msg == "Hel":
        msg = msg + letra
    elif letra == "o" and msg == "Hell":
        msg = msg + letra
    elif letra == " " and msg == "Hello":
        msg = msg + letra
    elif letra == "W" and msg == "Hello ":
        msg = msg + letra
    elif letra == "o" and msg == "Hello W":
        msg = msg + letra
    elif letra == "r" and msg == "Hello Wo":
        msg = msg + letra
    elif letra == "l" and msg == "Hello Wor":
        msg = msg + letra
    elif letra == "d" and msg == "Hello Worl":
        msg = msg + letra
    time.sleep(0.05)
    

os.system('cls')
    
print(msg + " (;")