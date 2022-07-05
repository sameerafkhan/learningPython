flavor_icecream = input('Enter a flavor: ')
Topping = input('Enter a topping: ')
cup_size = input('Enter a cup size: ')

if flavor_icecream == 'vanilla':
    Topping == 'chocolate chips'
    cup_size == 'large'
    print('Enjoy your', flavor_icecream, 'Icecream')
elif flavor_icecream == 'chocolate':
    Topping == 'cherry'
    cup_size == 'medium'
    print('Enjoy your', flavor_icecream, 'Icecream')
elif flavor_icecream == 'strawberry':
    Topping == 'almond'
    cup_size == 'small'
    print('Enjoy your', flavor_icecream, 'Icecream')
elif flavor_icecream == 'mango':
    Topping == 'pistachios'
    cup_size == 'large'
    print('Enjoy our seasonal', flavor_icecream, 'icecrame flavor')
else:
    print('Have a nice day!')


