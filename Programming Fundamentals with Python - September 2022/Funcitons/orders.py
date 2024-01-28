def orders(product, qnt):
    total = 0

    products_dict = {'coffee': 1.50,
                     'water': 1.00,
                     'coke': 1.40,
                     'snacks': 2.00}

    if product in products_dict.keys():
        total = products_dict[product] * qnt

    return f'{total:.2f}'


products = input()
quantity = int(input())

print(orders(products, quantity))
