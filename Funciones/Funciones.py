def una_funcion():
  print('función invocada.')

una_funcion()

# argumento arbitrario
def otra_funcion(*valores):
  print(valores)

otra_funcion("Hola", ' ', "Mundo!!!")
