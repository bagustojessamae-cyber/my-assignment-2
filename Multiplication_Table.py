﻿while(True):
   rows = int(input('Enter Row: '))
   col = int(input('Enter Col: '))
   search = int(input('Search a number: '))


   if(rows<=0 or col<=0):
       print('Invalid Input. Loop is stopped.')
       break;


   #for x in range(1, rows+1):    // kapag gusto mong iprint muna matrix bago mag-search ng number para ma-highlight
       #for y in range(1, rows+1):
           #print(x*y, end=" ")
          
       #print()
       #tas ilipat dito yung search chuchu


   for x in range(1,rows+1):
       for y in range(1,col+1):
           value = x*y
           if(search==value):
               print(f'[{value}]', end=" ")
           else:
               print(value,end=' ')
       print()