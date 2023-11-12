from os import system
class Persona():
    def __init__(self,nombre,apellido):
        self.nombre= nombre
        self.apellido= apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, cuenta_bancario, balance):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta_bancaria = cuenta_bancario
        self.balance = float(balance)
        
    def __str__(self):
        return f"Nombre: {self.nombre}, {self.apellido}, Balance:, {self.balance}"
    
    def deposito(self, cantidad):
        self.balance += cantidad
        print("Deposito aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")
def crear_usuario():
    nombres=input("\nIngrese su primer Nombre: ")
    apellidos=input("\nIngrese sus Apellidos: ")
    cuentabanco = input("Ingresa la cuenta bancaria: ")
    usuario = Cliente(nombres, apellidos, cuentabanco, 0)
    return usuario



def menu():
    system("cls")
    continua = False
    usuario = crear_usuario()
    while not(continua):
        system("cls")
        print(f"\n\t\t\t{usuario}")
        opc = input("""
        \t\tMENU
              
        'D' = Depositar
        'R' = Retirar
        'S' = Salir 
              """)
        match opc:
            case "d" | "D":
                monto_dep = int(input("Monto a depositar: "))
                usuario.deposito(monto_dep)
            case "r" | "R":
                monto_ret = int(input("Monto a retirar: "))
                usuario.retirar(monto_ret)            
            case "S" | "s":
                continua = True
                system("cls")
                print("Adios...")
menu()
