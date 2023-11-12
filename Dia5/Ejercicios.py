import os;


def menu():
    opc = 0
    while opc <= 4:
        os.system("cls");
        opc = int(input("Bienvenido\n\t\tIngresa la opcion que deceas:\n\t1-Distintos.\n\t2-Palabras.\n\t3-Numero 0.\n\t4-Numeros primos.\n\t0-Salir.\n\t"))
        match opc:
            case 1:
                num1, num2, num3 = int(input("\n\tDime un numero: ")), int(input("\n\tDime un numero: ")), int(input("\n\tDime un numero: "))
                numeros_distintos(num1, num2, num3);
            
            case 2:
                nombre = input("\n\tDime un nombre :")
                letras_nombre(nombre);
                os.system("pause")

            case 3:
                lista = []
                for numero in range(0,10):
                    lista.append(input(f"Dime el numero {numero}: "))
                resultado = numero_repetido(lista);
                print(resultado)
                os.system("pause")
            case 4:
                limite = int(input("Dime el limite de los numeros que quieres comprobar: "))
                print (numeros_primos(limite));
                os.system("pause")
            case 0:
                break;
            case _:
                continue


def numeros_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    numeros = [num1, num2, num3]
    if suma > 15:
        print("El numero mayor es: ",max(numeros))
    elif suma < 10:
        print("El numero menor es: ",min(numeros))
    else:
        numeros.sort()
        print("El numero central es: ",numeros[1])
    os.system("pause")

def letras_nombre(nombre):
    letras = set()
    for letra in nombre:
        letras.add(letra)
    lista = list(letras)
    lista.sort()
    lista.reverse
    print(lista)
    os.system("pausa")

def numero_repetido(lista):
    contador = 0
    for i in lista:
        if contador != 2: 
            if i == '0':
                contador +=1
                print(contador)
            else:
                contador = 0
        else:
            
            return True
    
    return False
def numeros_primos(limite):
    primos = [2]
    iteracion = 3
    if limite < 2:
        return 0
    while iteracion <= limite:
        for n in range(3, iteracion, 2):
            
            if iteracion % n ==0:
                iteracion +=2
                break
        else:
            primos.append(iteracion)
            iteracion+=2
    print(primos)
    return len(primos)

menu();
