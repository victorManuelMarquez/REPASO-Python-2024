# los diccionarios son mutables, "ordenados" y no permiten claves duplicadas.
diccionario = {
  "Nombre Completo":"Juan Perez",
  "Edad":47,
  "Nro. de cuenta":"00000024284010422",
  "Saldo":8420.42
}

print("Diccionario original:\n", diccionario, sep='')

diccionario["Saldo"] += 10000.0

# muestro clave y valor mediante un foreach
for c, v in diccionario.items():
  print(c, ':', v)
