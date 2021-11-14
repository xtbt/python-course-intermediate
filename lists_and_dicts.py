def main():
    my_list = [1, 'Hello', True, 4.5]
    my_dictionary = {"firstname": "Jonathan", "lastname": "Sánchez"}

    super_list = [
        {"firstname": "Ingrid", "lastname": "Sánchez"},
        {"firstname": "Ángel", "lastname": "Vargas"},
        {"firstname": "Alberto", "lastname": "Sánchez"},
        {"firstname": "Oralia", "lastname": "Barroterán"},
        {"firstname": "Luis", "lastname": "Luna"}
    ]

    super_dictionary = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43,8.8],
        "strings": ['Hello', 'World', 'Happy', 'Not']
    }

    for key, value in super_dictionary.items():
        print(str(key) + ' - ' + str(value))
    
    for item in super_list:
        print(item)


if __name__ == '__main__':
    main()