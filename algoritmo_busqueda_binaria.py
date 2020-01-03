numero_Usuario = int(input("Escribe un numero entero : "))
epsilon = 0.0001
limite_inferior = 0.0
limite_superior = max(1.0, numero_Usuario)
respuesta = (limite_superior+limite_inferior)/2
paso = epsilon ** 2

while abs(respuesta ** 2 - numero_Usuario) >= epsilon:
    print(
        f'limite inferior es : {limite_inferior} y limite superior es : {limite_superior} la respuesta es : {respuesta}')
    if respuesta ** 2 < numero_Usuario:
        limite_inferior = respuesta
        # respuesta += paso
        # print(f'No se encontro una raiz cuadrada para el {numero_Usuario}')
    else:
        limite_superior = respuesta

    respuesta = (limite_superior + limite_inferior) / 2
print(f'La raiz cuadrada de {numero_Usuario} es {respuesta}')
