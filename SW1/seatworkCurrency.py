def convert_Indian(d):
   return f'{indian * d:.2f} INR'


def convert_British(d):
   return f'{british * d:.2f} GBP'


def convert_China(d):
   return f'{chinese * d:.2f} CNY'


indian = 88.05
british = 0.73
chinese = 7.114


while True:
   dollar = input('Enter dollar($) (* to exit): ')
  
   dElement = dollar.split('@')
   listDollar = []
  
   if not all(char.isdigit() for char in dElement or dollar == '*'):
       print("bye")
       break


   else:
       for d in dElement:
           listDollar.append(float(d))


   print(f'{"Dollar($)":<10} {"Indian Ruppe(R)":<15} {"British(Pound)":<15} {"China(Y)"}')


   for d in listDollar:
       print(f'{d:<10} {convert_Indian(d):<15} {convert_British(d):<15} {convert_China(d)}')