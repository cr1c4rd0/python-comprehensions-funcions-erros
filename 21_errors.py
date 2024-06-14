#print(0/0)

#suma = lambda x,y: x + y
#assert suma(2,2) == 4

#age = 10
#if age < 18:
 #   raise Exception('No se permiten menores de edad')

try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
    print(error)

print('Hola')

Numbers = "0123456".find('1')

print(Numbers)