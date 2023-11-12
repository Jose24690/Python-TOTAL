import os;

nombre = input("Cual es tu nombre? ");
ventas = int(input("Cuantas ventas tuviste este mes? "));

pago = round((ventas *13)/100.2);
os.system("cls");

print(f"Hola, {nombre}, tu pago del mes es de: ${pago}");