def suma(a, b):
    total = a+b
    return total


print(suma(2, 1))


def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'


print(nombre_completo('Alejandro', 'Upegui'))
print(nombre_completo('Alejandro', 'Upegui', inverso=True))
print(nombre_completo(apellido='Upegui', nombre='Alejandro'))
