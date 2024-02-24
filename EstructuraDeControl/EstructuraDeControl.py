# casting de string a un número entero.
numero = int(input('Ingrese un número: '))
if numero % 2 > 0:
  print(numero, 'es impar.')
else:
  print(numero, 'es par.')
print(numero, end=" ")
print('es positivo') if numero > 0 else print('es negativo')
numero2 = int(input('Ingrese otro número: '))
# ternario
print(numero, '>', numero2) if numero > numero2 else print('ambos números son iguales') if numero == numero2 else print(numero2, '>', numero)

lista = []
diccionario = {}
seguir = True
while (seguir):
  print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
  print('Cargar una lista: 1')
  print('Cargar un diccionario: 2')
  print('Ingrese 0 para salir.')
  # disponible desde la versión 3.11
  match int(input('Ingrese su opción: ')):
    case 1:
      lista.append(input('Ingrese un dato: '))
    case 2:
      clave = input('Ingrese la clave: ')
      valor = input(f'Ingrese un valor para {clave}: ')
      diccionario[clave] = valor
    case 0:
      seguir = False
  print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(*lista, sep=" ") if len(lista) > 0 else print('Lista vacía.')
print('Diccionario: ', diccionario)