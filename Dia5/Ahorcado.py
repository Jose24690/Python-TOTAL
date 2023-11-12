from random import choice
import os
import sys

palabras=[
    "casa","amigo","coche","barco","estupendo","barriga","consejo",
    "buho","arbitro","deporte","corazon","amor","ciudad","pajaro",
    "hueso","chico","chica","mapa","campo","tarta","television",
    "decoracion","mueble","mesa","paloma","tigre","sillon","agenda",
    "calendario","mechero","vaso","botella","perro","casco","leon",
    "pantera","pelicano","madera","metal","agua","solido","gas","silla",
    "libro","cesta","pizarra","planta","basura","collar","pijama","alicate",
    "hucha","horno","botella","ahorcado","raton","alcohol","medicamento",
    "guerra","paz","camiseta","fuego","tierra","planeta","sol","luna",
    "jupiter","urano","pluton","libreta","marte","mercurio","venus",
    "galaxia","universo","guitarra","musica","piano","cenicero","tambor",
    "arte","artesania","violin","gato","correr","saltar","saturno","estrella",
    "violin"
    
]
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def definir_palabra(lista_palabras):
    palabra = choice(lista_palabras)
    letras_unicas = len(set(palabra))

    return palabra, letras_unicas

def ingresar_letra():
    letra_valida = False
    letra = "a"
    abcedario="abcdefghijklmnñopqrstuvwxyz"
    while not letra_valida:
        
        sys.stdout.flush()
        letra = input("Dime la letra que vas a ingresar: ".lower())
        
        if letra in abcedario and len(letra) == 1:
            
            letra_valida = True
        else:
            print("Por favor ingresa una letra valida, solo un caracter:")
    return letra

def mostrar_tablero(palabra_elegida):
    print(f"Tienes un total de {intentos} intentos.\nLetras incorectas: {letras_incorrectas}\nLetras correctas: {letras_correctas}\n\t")
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

def letra_correcta(palabra_elegida, letra, vidas, coincidencias ):
    fin = False
    if letra in palabra_elegida:
        letras_correctas.append(letra)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra)
        vidas -= 1
    if vidas == 0:
        fin = perder();
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_elegida);

    return fin, vidas, coincidencias 

def perder():
    print(f"Haz perdido :(\n\t La palabra elegida era: "+palabra)
    os.system("pause")
    juego_nuevo();
    os.system("pause")

def ganar(palabra_encontrada):
    print("\n\tFelicidades! Ganaste!!")
    mostrar_tablero(palabra_encontrada)
    os.system("pause")
    juego_nuevo();
    


def juego_nuevo():
    opc = 1
    while opc < 3  and opc > 0:
        opc = input("\n\n\t\tQuires jugar otra vez??\n\t1-Si\n\t2-No")
        if opc == 1:
            letras_correctas = []
            letras_incorrectas = []
            intentos = 6
            aciertos = 0
            definir_palabra();
            return False
        else: 
            return True


palabra, letras_unicas = definir_palabra(palabras)

while not juego_terminado:
    os.system("cls")
    print("*"*20)
    mostrar_tablero(palabra)
    #print('\nLetras incorrectas: ' + '-'.join(letras_incorrectas))
    #print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = ingresar_letra()

    terminado, intentos,  aciertos = letra_correcta(palabra,letra,intentos,aciertos)

    juego_terminado = terminado


    
        
