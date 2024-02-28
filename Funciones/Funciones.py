def una_funcion():
  print('función invocada.')

una_funcion()

# argumento arbitrario
def otra_funcion(*valores):
  print(valores)

otra_funcion("Hola", ' ', "Mundo!!!")

# argumento predeterminado
def funcion_pred(arg = 1000):
  print('valor recibido :', arg)

funcion_pred()

# argumentos arbitrarios posicionales
def nueva_funcion(**valores):
  print(valores)
  
nueva_funcion(arg1='Juan Perez', arg2=24, arg3=True)