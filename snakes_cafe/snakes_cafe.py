print('''
  **************************************
  **    Welcome to the Snakes Cafe!   **
  **    Please see our menu below.    **
  **
  ** To quit at any time, type "quit" **
  **************************************

  Appetizers
  ----------
  Wings
  Cookies
  Spring Rolls

  Entrees
  -------
  Salmon
  Steak
  Meat Tornado
  A Literal Garden

  Desserts
  --------
  Ice Cream
  Cake
  Pie

  Drinks
  ------
  Coffee
  Tea
  Unicorn Tears

  ***********************************
  ** What would you like to order? **
  ***********************************
''')

# create snake cafe dictionary
Snake_cafe = {
    'wings' : 0,
    'cookies' : 0,
    'spring rolls' : 0,
    'salmon' : 0,
    'steak' : 0,
    'meat tornado' : 0,
    'a literal garden' : 0,
    'ice cream' : 0,
    'cake' : 0,
    'pie' : 0,
    'coffee' : 0,
    'tea' : 0,
    'unicorn tears' : 0
}

while True:
    order = input('> Order: ')
    if order == 'quit':
        break
    if order.lower() in Snake_cafe:
        Snake_cafe[order.lower()] += 1
        if Snake_cafe[order.lower()] == 1:
            print('**', f'1 order of {order} have been added to your meal', '**')
        else:
            print('**', f'{Snake_cafe[order.lower()]} order of {order} have been added to your meal', '**')    
