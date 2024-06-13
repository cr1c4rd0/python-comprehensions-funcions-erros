def suma_range(min, max):
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

result = suma_range(1, 10)
print(result)
result2 = suma_range(result, result + 10)
print(result2)
