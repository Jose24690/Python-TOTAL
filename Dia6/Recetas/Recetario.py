from os import system
import os
from pathlib import Path
mi_ruta = Path("E:\Practicas\python\PhytonTotal\Dia6\Recetas")


def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador

def mostrar_categorias(ruta):
    system("cls")
    print("\t\tCategorias:\n")
    ruta_categorias = Path(ruta)
    lista_categorias = []

    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

def seleccionar_categorias(categorias):
    categorias_numero = len(categorias)
    opc = 1
    while opc < categorias_numero + 1:
        opc = int(input("Dime la categoria a la que quieres entrar: "))
        system("cls") 
        if opc > 0 and opc <categorias_numero + 1 :
            return categorias[int(opc) - 1]
        else :
            print(f"Seleccione una opcion valida entre el 1 y {categorias_numero}")
            opc = 1

def mostrar_recetas(seleccion):
    system("cls")
    print("\tRecetas")
    lista_recetas = []
    contador = 1;
    ruta_recetas = Path(seleccion);
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas

def seleccionar_receta(recetas):
    numero_recetas = len(recetas)
    opc = 1
    while opc < numero_recetas + 1:
        opc = int(input("Dime la receta que quieres leer: "))
        system("cls") 
        if opc > 0 and opc <numero_recetas + 1 :
            return recetas[int(opc) - 1]
        else :
            print(f"Seleccione una opcion valida entre el 1 y {numero_recetas}")
            opc = 1


def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(selecion):
    receta_existe = False

    while not receta_existe:
        nombre_receta = input("Dime el nombre de tu receta: ")
        nombre_receta = nombre_receta + '.txt'
        contenido_receta = input("Escribe tu nueva receta\n\t")
        ruta_nueva = Path(selecion, nombre_receta)
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            receta_existe = True
        else:
            system("cls")
            print("Lo siento, esa receta ya existe : (\n")

def crear_categoria(ruta):
    system("cls")
    categoria_existe = False

    while not categoria_existe:
        nombre_categoria = input("Dime el nombre de tu categoria: ")    
        ruta_nueva = Path(ruta, nombre_categoria)
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            categoria_existe = True
        else:
            system("cls")
            print("Lo siento, esa categoria ya existe : (\n")
def eliminar_receta(selecion):
    opc = 3
    while opc > 0 and opc >2:
        system("cls")
        opc = int(input("""Estas seguro de querer eliminar esta receta:
                    1-Si
                    2-No
                    """))
        if opc == 1:
            Path(selecion).unlink();
            print(f"La receta {selecion.name} ha sido eliminada")
        elif opc == 0:
            print(f"La receta {selecion.name}  no ha sido eliminada")
        else:
            print("Seleciona una opcion valida")

def eliminar_categoria(selecion):
    opc = 3
    while opc > 0 and opc >2:
        system("cls")
        opc = int(input("""Estas seguro de querer eliminar esta categoria:
                    1-Si
                    2-No
                    """))
        if opc == 1:
            Path(selecion).rmdir();
            print(f"La categoria {selecion.name} ha sido eliminada")
        elif opc == 0:
            print(f"La categoria {selecion.name}  no ha sido eliminada")
        else:
            print("Seleciona una opcion valida")


def menu(programa_continua):
    while not programa_continua:
        system("cls")
        print(f"Las recetas se encuentran en {mi_ruta}")
        print(f"Total recetas: {contar_recetas(mi_ruta)}\n\n")
        opc = input("""\t\tBienvenido al administrador de recetas 
            Por favor indica la opcion deceada.
            1-Leer receta.
            2-Crear receta.
            3-Crear categoria.
            4-Eliminar receta.
            5-Eliminar categoría.
            0-Salir.
            """)
        match opc:
            case "1":
                categorias  = mostrar_categorias(mi_ruta)
                seleccion = seleccionar_categorias(categorias);
                receta = mostrar_recetas(seleccion);
                if len(receta) < 1:
                    print("no hay recetas en esta categoría.")
                else:
                    receta_selec = seleccionar_receta(receta);
                    leer_receta(receta_selec);
                system("pause")
            case "2":
                categorias  = mostrar_categorias(mi_ruta)
                seleccion = seleccionar_categorias(categorias);
                crear_receta(seleccion)
            case "3":
                crear_categoria(mi_ruta);
            case "4":
                categorias  = mostrar_categorias(mi_ruta)
                seleccion = seleccionar_categorias(categorias);
                receta = mostrar_recetas(seleccion);
                receta_selec = seleccionar_receta(receta);
                eliminar_receta(receta_selec);
            case "5":
                categorias  = mostrar_categorias(mi_ruta)
                seleccion = seleccionar_categorias(categorias);
                eliminar_receta(seleccion);
            case "0":
                system("cls")
                print("Adios :) ...")
                return True
menu(False);