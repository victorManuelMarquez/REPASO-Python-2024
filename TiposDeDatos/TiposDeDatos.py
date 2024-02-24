# tipos de datos básicos
entero = 1392
# muestro el valor y el tipo de dato; sep evita que se agreguen los espacios entre las comas.
print('Entero: valor:=', entero, '; tipo:=', type(entero).__name__, sep="")
flotante = 13.932
print('Flotante: valor:=', flotante, '; tipo: :=', type(flotante).__name__, sep="")
boleano = True
print('Booleano: valor:=', boleano, '; tipo:=', type(boleano).__name__, sep="")
cadena = "Hola Mundo!!!"
print('Cadena: valor:=', cadena, '; tipo:=', type(cadena).__name__, sep="")
nulo = None
print('Sin determinar: valor:=', nulo, '; tipo:=', type(nulo).__name__, sep="")
# tipos de datos complejos
lista = ["Mutable", 24, True, 32.2]
print('Lista: valores:=', lista, '; tipo:=', type(lista).__name__, sep="")
tupla = (23, False, 11.23, 'Inmutable')
print('Tupla: valores:=', tupla, '; tipo:=', type(tupla).__name__, sep="")
rango = range(10)
print('Rango: valores:=', *rango, '; tipo:=', type(rango).__name__, sep="")
diccionario = {24 : "Juan", 29 : "Mónica", 34 : "Pablo"}
print('Diccionario: valores:=', diccionario, '; tipo:=', type(diccionario).__name__, sep="")
vector = {'A', 23, 0.2, True}
print('Set: valores:=', vector, '; tipo:=', type(vector).__name__, sep="")
# tipos de datos "no tan habituales"
complejo = 3.14j
print('Complejo: valor:=', complejo, '; tipo:=', type(complejo).__name__, sep="")
vector_estatico = frozenset({'"Enero"', '"Febrero"', '"Marzo"'})
print('Set estático: valores:=', *vector_estatico, '; tipo:=', type(vector_estatico).__name__, sep="")
crudo = b"valor en bytes"
print('Bytes: valor:=', crudo, '; tipo:=', type(crudo).__name__, sep="")
array_crudo = bytearray(crudo)
print('ByteArray: valor:=', array_crudo, '; tipo:=', type(array_crudo).__name__, sep="")
direccion_de_memoria = memoryview(array_crudo)
print('MemoryView: valor:=', direccion_de_memoria, '; tipo:=', type(direccion_de_memoria).__name__, sep="")