def una_funcion():
  print('función invocada.')

una_funcion()

# argumento arbitrario
def otra_funcion(*valores):
  print(valores)

otra_funcion("Hola", ' ', "Mundo!!!")

# argumento predeterminado
def funcion_pred(arg = 1000)
  print('valor recibido :', arg)

funcion_pred()
