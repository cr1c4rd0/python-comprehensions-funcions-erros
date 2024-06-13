price = 100 # Global

def increment():
    price = 10 # Local
    return price

print(price)
price2 = increment()
print(price2)