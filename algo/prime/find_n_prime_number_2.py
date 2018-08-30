#!/usr/bin/python

limit=600851475143
#limit=90

def get_greater_prime_div(limit):
  b=limit
  greater_div = 0
  while(b > 0):
    a = limit 
    while(a < b):
      if b != 2 and ( b % 2) == 0:
        break
      if b != 3 and ( b % 3) == 0:
        break
      if b != 5 and ( b % 5) == 0:
        break
      if a != 1 and ( b % a ) == 0 :
        break
      a -=1
      if a == b:
        print(b)
        if ( limit % b ) == 1:
          greater_div = b 
          return greater_div
    b -=1
  return greater_div 

greater_div= get_greater_prime_div(limit)


print(greater_div)

