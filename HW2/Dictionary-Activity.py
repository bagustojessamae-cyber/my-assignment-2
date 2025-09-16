dict_items = {}


size = int(input('Matrix Size: '))


for i in range(size):


   value = input(f'Shopping Items {i+1}: ')
   dict_items[i] = value


print('You have 3 items in the cart.')


while True:


   print('What would you like to do?')
   action = input('[C]hange items' \
         '[R]emove' \
         '[D]isplay,' \
         '[S]earch')
  
   if action.lower() == 'c':
       keyToSearchC = int(input('Enter key to search: '))


       valueC = dict_items.get(keyToSearchC)
       if valueC is not None:
           print(f'Found {valueC} item')
           newValueC = input('Enter Value: ')
           dict_items[keyToSearchC] = newValueC
       else:
           print("I'm sorry, not in the cart.")


   elif action.lower() == 'r':
       keyToSearchR = int(input('Enter key to search: '))


       valueR = dict_items.get(keyToSearchR)
       if valueR is not None:
           print(f'The key {keyToSearchR} with value {valueR} has been deleted.')
           del dict_items[keyToSearchR]
       else:
           print('Key not found.')


   elif action.lower() == 'd':
       print('Displaying Values')
       print('Key Value')
       for key, value in dict_items.items():
           print(f'{key} {value}')


   elif action.lower() == 's':
       itemToSearch = input('Enter item to search: ')
       found = False


       for key, value in dict_items.items():
           if itemToSearch.lower() == value.lower():
               print(f'Found {value} item')
               found = True
               break
       if not found:
           print("I'm sorry, not in the cart.")


   else:
       print('Bye')
       break