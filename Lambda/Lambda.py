# Función anónima lambda
potencia = lambda x, y : x ** y

# Función estándar invocando a la función lambda
def cuadrado(n):
    return f"{n} ^ 2 = {potencia(n, 2)}"

# Usos prácticos
print(cuadrado(int(input("Ingrese un número para elevarlo al cuadrado: "))))
print("Ok. Ahora otro número...")
print(potencia(int(input("Ingrese la base: ")), int(input("Ingrese el exponente: "))))
print("Fin del programa.")