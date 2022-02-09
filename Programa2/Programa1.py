import math

def calculaRaiz(num1):
    
    if num1<0:
        raise ValueError ("El número no puede ser negativo")
    else:
        return math.sqrt(num1)
    
def Division(num1, num2):
    
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación erronea"
    

print("-----Menú división y raiz cuadrada-----")
print("1. División")
print("2. Raiz cuadrada")

try:
    op = (int(input("Introduce un numero: ")))
    if op == 1:
        try:
            opc1 = int(input("Ingrese el primer número: "))
            opc2 = int(input("Ingrese el segundo número: "))
            print(Division(opc1,opc2))
        except ValueError:
            print("Valores no validos")
    
    elif op == 2:
        try:
            opc1 = int(input("Ingrese un número: "))
            try:
                print(calculaRaiz(opc1))
                
            except ValueError as ErrorDeNumero:
                
                print(ErrorDeNumero)
                
            finally:
                print("El programa terminó")
        except ValueError:
            print("Valor no valido")
    else:
        print("Opción no valida")
except ValueError:
    print("Opción no valida")
    
    
    
    