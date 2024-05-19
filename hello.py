import string
import random
import time
import os

lista = list(string.printable)

for i in range(5):
    lista.pop(-1)
msgfinal = ""
letra = ""

for i in "Hello World":
    while letra != i:
        letra = random.choice(lista)
        print(msgfinal + letra)
        time.sleep(0.03)
    msgfinal = msgfinal + letra
os.system('cls')
    
print(msgfinal + " (;")