respuesta = 0;
numero_Usuario = int(input("Escribe un numero entero : "))

while respuesta **2 < numero_Usuario:
    respuesta += 1
if respuesta ** 2 == numero_Usuario:
    print(f'La raiz cuadrada de {numero_Usuario} es {respuesta}')
else:
    print(f'No se encontro una raiz cuadrada para el {numero_Usuario}')
