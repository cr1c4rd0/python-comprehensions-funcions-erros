# pregunta sobre el sistema operativo
import sys 
print(sys.path) # muentra la ruta donde se esta ejecutando 

# modulo para expresiones regulares
import re
text = 'Mi numero de telefono es: 311 123 121, el codigo del país es 57, numero de la suerte 7'
result = re.findall('[0-9]+', text)
print(result)

# manejo de horas y fechas
import time
timestamp = time.time()
print(timestamp)
local = time.localtime()
result_2 = time.asctime(local)
print(result_2)

# utilidad para manejar listas
import collections
numbers = [1,1,2,2,3,3,4,4]
counter = collections.Counter(numbers)
print(counter)