import functools

numbers = [1, 2, 3, 4]
total = functools.reduce(lambda counter, item: counter + item, numbers)

print(total)

def accum(counter, item):
    print('counter: ', counter)
    print('item: ', item)
    return counter + item

total_2 = functools.reduce(accum, numbers)
print(total_2)