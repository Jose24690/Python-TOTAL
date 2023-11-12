from random import *
import os
import sys

palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def definir_palabra(lista_palabras):
    palabra = choice(lista_palabras)
    letras_unicas = len(set(palabra))
    print(letras_unicas)

    return palabra, letras_unicas
input("hola")