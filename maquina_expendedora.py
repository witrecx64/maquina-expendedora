import sys 
import time
print("----------------------------------------------")
print("----------------------------------------------")
print("----------------------------------------------")
print("-------Chocorramo-----------------------------")
print("-------Chococosoo-----------------------------")
print("-------Bimbo_choco----------------------------")
print("-------Bimbo_vainilla-------------------------")
print("-------Cocholate_chips------------------------")
print("----------------------------------------------")
print("----------------------------------------------")

#chocorramo = 2500

#chocosoo = 2000

#Bimbo_choco = 1550

#Bimbo_vainilla = 3000

#Cocholate_chips = 1200

producto_norm = str(input("Ingrese su producto: "))
producto = producto_norm.lower()

for i in range (2):
    if producto == "chococosoo":
        costo_producto = 2000
        break
    elif producto == "bimbo_choco":
        costo_producto = 1550
        break
    
    elif producto == "chocolate_chips":
        costo_producto = 1200
        break
    elif producto == "chocorramo":
        costo_producto = 2500
        break
    elif producto == "bimbo_vainilla":
     costo_producto = 3000
     break
    else:
        time.sleep(3)
        print("Ha introducido de forma incorrecta su artuculo")
        time.sleep(5)
        repetir = input("Quiere repetir el programa cancele la terminal ctrl+c o ctrl+z+enter o no ponga nada: ")
        if repetir == "":
            sys.exit()
            
        else:
            continue
        
        




costo = costo_producto

print("El costo es: ", costo)


ingresado = int(input("Ingrese dinero: "))

cambio = ingresado - costo
if cambio < 0:
    print("Saldo insuficiente")
    sys.exit() 
else: 
    while True:
        
        print("Calculando cambio. ")
        time.sleep(1)
        print("Calculando cambio. .")
        time.sleep(1)
        print("Calculando cambio. . .")
        time.sleep(1)
        print("Calculando cambio. ")
        time.sleep(1)
        print("Calculando cambio. .")
        time.sleep(1)
        print("Calculando cambio. . .")
        time.sleep(1)
        break
    
    


def calcular_cambio(cambio: int)->str:
    a = cambio // 500
    cambio = cambio % 500
    b = cambio // 200
    cambio = cambio % 200
    c = cambio // 100
    cambio = cambio % 100
    d = cambio // 50
    return str(a) + " Monedas de 500     " + str(b) + " Monedas de 200     " + str(c) + " Monedas de 100    " + str(d) +" Monedadas de 50"

resultado = calcular_cambio(cambio = cambio)
print("Su cambio total es de: ",resultado)
print(cambio, " Pesos")