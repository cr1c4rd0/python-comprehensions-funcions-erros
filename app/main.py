import utils

data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country': 'Bolivia',
        'Population': 300
    }
]

def run():
    keys, values = utils.get_population()
    print(keys, values)


    country = input('Tipe Country: ')

    result = utils.population_by_country(data, country)
    print(result)

# Dice al archivo main que si es ejecutado desde la termina se ejecute y si es por otro archivo tambien 
if __name__== '__main__':
    run()