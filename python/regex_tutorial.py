import re

text = "carlos.nieto@gmail.com"

# Definir un patron
pattern = re.compile("[\w\.]+@[a-z]+\.[a-z]+")

# Obtener un iterator de matches en un texto
result = re.finditer(pattern, text)

# Obtener el match en string:
match = list(result)[0]
match.group()

# Obtener el índice donde empieza/termina el match
match.start()
match.end()

# Obtener todas las subsecuencias de matches dentro de un texto en una lista
substrings = re.findall(pattern, text)

# Obtener una lista dividida por el patrón
split_list = re.split(pattern, text)