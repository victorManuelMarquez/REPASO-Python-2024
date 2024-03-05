lista = ['contenido', 12, 7.8, True]

print(lista)

print("bucle for:")

for i in range(len(lista)):
  print(lista[i])

print("bucle while:")

i = 0
while i < len(lista):
  print(lista[i])
  i += 1

print("comprensión: ", end='')

[print(valor, end=' ') for valor in lista]

print("Fin del programa.")