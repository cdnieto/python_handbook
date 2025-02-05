"""
Definition:
Iterable objects are any object that can be used in a for loop. Ejemplos:
- list
- tuple
- set
- dictionary
- string

Los items en una lista se iteran de manera ordenada, mientras que los items en un set
se iteran de manera desordenada.

Al iterar en un diccionario solo iteramos en las keys. Para iterar en las keys y los values
hay que llamar el método dict.items() -> itera en tuplas de (key, value).

Less visual objects:
- range()
- enumerate()

¿Cómo sabemos que tenemos un iterable?
Fácil: le podemos aplicar la función iter(iterable). Esta función regresa un objeto especial:
Un range_iterator.

Iterator - An object knowing how to retrieve consecutive elements from an iterable one by 
one. Un objeto que sabe como extraer elementos consecutivos de un iterable uno por uno.

A un iterator, se le puede aplicar la función next(iterator), la cual extrae de manera ordenada
los elementos del iterator con cada vez que se llama sobre el iterator.

Cuando ya no hay más valores dentro del iterator que puedan ser extraídos, la función next(iterator)
va a arrojar un StopIteration exception para dejar de iterar.
"""

# ¿Por qué es importante el `iterator` para un `ìterable?
# Veamos cómo un ciclo `for` funciona tras bambalinas.
# Es lo mismo hacer un ciclo `for` de la siguiente manera:
droids = ['R2-D2', 'TC-16', 'C-3PO']
for droid in droids:
    print(droid)

# Que hacer el siguiente while loop:
iter_droids = iter(droids)
while True:
    try:
        droid = next(iter_droids)
        print(droid)
    except StopIteration:
        break
