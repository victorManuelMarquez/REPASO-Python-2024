# un set no permite duplicados y no preserva el orden de los elementos.
miSet = {1, "Valor", True, False, 'a', 0, 24, 4.2} # Boleanos y 0 - 1 se consideran similares.

[print(valor, end=' ') for valor in miSet]

print('\nFin del programa.')