numero_1 = int(input("Escribe el primer numero"))
numero_2 = int(input("Escribe el segundo numero"))
if numero_1 > numero_2:
    print(f'El numero {numero_1} es mayor que el numero {numero_2}')
elif numero_1 == numero_2:
    print(f'El numero {numero_1} es igual al numero {numero_2}')
else:
    print(f'El numero {numero_1} es menor al numero {numero_2}')