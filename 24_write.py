# r+ da permiso de escritura pero conservando la data que ya tienen el archivo mientras w+ va a sobre escribir todo el archivo.
with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)

    file.write('\nnuevas cosas en este archivo')
