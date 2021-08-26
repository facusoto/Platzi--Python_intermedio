def run():
    my_list = [11, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "Soto"}

    super_list = [
        {"firstname": "Facundo", "lastname": "Soto"},
        {"firstname": "Miguel", "lastname": "Soto"},
        {"firstname": "Pablo", "lastname": "García"},
        {"firstname": "Daniel", "lastname": "Martinez"},
        {"firstname": "Franco", "lastname": "L."},
        {"firstname": "Martín", "lastname": "Aquino"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, 2, 0, -4],
        "floating_nums": [1.1, 1.9, 2.0, 7.9]
    }

    for key, value in super_dict.items():
        print(f'{key} - {value}')

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')

if __name__ == '__main__':
    run()