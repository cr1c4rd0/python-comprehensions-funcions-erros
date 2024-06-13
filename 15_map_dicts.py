items = [
    {
        'producto': 'camisa',
        'precio': 100
    },
    {
        'producto': 'pantalon',
        'precio': 300
    },
    {
        'producto': 'gorra',
        'precio': 50
    }
]

prices = list(map(lambda item: item['precio'], items))
print(prices)

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['precio'] * .19
    return new_item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)