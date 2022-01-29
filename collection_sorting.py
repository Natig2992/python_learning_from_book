#!/usr/bin/env python3

#All info about working with collections in Python:

shop = [('каретка', 1200), ('шатун', 1000), ('седло', 300),
        ('педаль', 100), ('седло', 1500), ('рама', 12000),
        ('обод', 2000), ('шатун', 200), ('седло', 2700)]

def prepare_item(item):
    return (item[0], -item[1])

shop.sort(key=prepare_item)

for det, price in shop:
    print('{:<17} цена: {:>3}р.'.format(det, price))
    # {:<17} and {:>3} - is offset by spaces 

# shop.sort(key=lambda x: (x[0], -x[1])) - alternative var instead of prepare_item function, it`s lambda builtin func;


for i in range(1,3):

    print()

a, b = [1, 2, 3], [4, 5]
c = [*a, *b]  # работает на версии питона 3.5 и выше, aster character removes nesting of lists
print(c)      # [1, 2, 3, 4, 5]

for i in range(1,3):

    print()

#copy() and update() methods for dictionaries collections: 
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)        	# {'a': 1, 'c': 3, 'b': 2, 'd': 4}

#Combining method for dictionaries in Python >= 3.5

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {**dict1, **dict2}
print(dict3)        	# {'a': 1, 'c': 3, 'b': 2, 'd': 4}
