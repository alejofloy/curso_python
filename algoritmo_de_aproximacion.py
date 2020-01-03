epsilon = 0.0001
paso = epsilon ** 2
respuesta = 0.0
numero_Usuario = int(input("Escribe un numero entero : "))

while abs(respuesta ** 2 - numero_Usuario) >= epsilon and respuesta <= numero_Usuario:
    print(abs(respuesta**2 - numero_Usuario), respuesta)
    respuesta += paso
if abs(respuesta ** 2 - numero_Usuario) >= epsilon:
    print(f'No se encontro una raiz cuadrada para el {numero_Usuario}')
else:
    print(f'La raiz cuadrada de {numero_Usuario} es {respuesta}')
