import os
from random import *

os.system("cls")

valor_random = randint(1,100);
nombre = input("Dime tu nombre: ")
intentos = 1
print("Bienvenido al juego 'Adivina el numero'")
while intentos < 9:
    numero = int(input(f"\n\n\t\tEsta es tu oportunidad numero: {intentos}, dime un numero: "))
    if numero > 100:
        print("\n\n\t\t\t'El numero es muy grande por favor ingresa un numero entre el 1 y el 100'")
    elif valor_random > numero:
        print("\n\tEl numero que buscas en mayor...")
    elif valor_random < numero:
        print("\n\tEl numero que buscas en menor...")
    else:
        print(f"\n\n\n\t\t\tFelicidades {nombre}\n\n\n\t\t\tHaz acertado el valor de el numero que buscabas es: {numero}")
    intentos +=1
if numero != valor_random:
    print("No conseguiste adivinar el numero :(")