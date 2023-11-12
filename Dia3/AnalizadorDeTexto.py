import os;
os.system("cls");

def analisador():
    texto = input("Dime el texto que deceas analisar: ");
    texto = texto.lower();
    letras = []
    
    for i in range(3):
        letras.append(input("\nDime la letra: \n".lower()))
        print("Hemos encontrado la cantidad de caracteres iguales a:",letras[i]," la cantidad de: ",texto.count(letras[i]));
    textoPalabras = texto.split();
    print("\nTermino la primera parte del codigo\n\n")
    palabra = input("Indicame cual es la palabra de la que quieres saber cuanto se repitio.")
    print("La palabra se repitio un total de: ",textoPalabras.count(palabra), " veces.");
    print("\nTermino la segunda parte del codigo\n\n")
    print("La primera letra del texto es: ",texto[0]," y la ultima letra es:", texto[-1])
    print("\nTermino la tercera parte del codigo\n\n")
    print("TEXTO INVERTIDO")
    palabras = textoPalabras
    palabras.reverse()
    texto_invertido = ' '.join(palabras)
    print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")
    print("\nTermino la cuarta parte del codigo\n\n")
    print(f"Tu texto tiene un total de: ", {len(textoPalabras)}, " palabras")
    print("Por ultimo el analisador nos dira si la palabra 'python'se encuentra en el texto\n\n")
    if (texto.find("python")):
        print ("Si se encuentra en el texto :)");
    else: 
        print("No se encuetra en el texto :(");
    print("gracias");
    os.system("pause");
    

analisador();



