L1 = [
    ('bread', 10),
    ('butter', 20),
    ('chocolate dark', 15),
    ('chocolate white', 17),
    ('cake', 19)
]


def sort_product(food):
    return food[1]


L1.sort(key=sort_product)


print(L1)
