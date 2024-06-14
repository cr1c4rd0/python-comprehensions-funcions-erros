file = open('./text.txt')
#print(file.read())

# para leer linea a linea como iterador
#print(file.readline())
#print(file.readline())
#print(file.readline())


for line in file:
    print(line)

file.close()

# abre y cierra el archivo automaticamente
with open('./text.txt') as file:
    for line in file:
        print(line)
