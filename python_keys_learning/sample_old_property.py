#http://www.trytoprogram.com/python-programming/python-property/
class CurrencyConverter:
 
 def __init__(self, currency_x = 1):
   self.currency_x = currency_x
   self.__currency_x = currency_x

 def currency_converter(self):
   currency_y = self.get_currency_x() * 28
   return (currency_y)

 #implementing new getter method
 def get_currency_x(self):
   print ('inside getter method')
   return (self._currency_x)

 #implementing new setter method
 def set_currency_x(self, currency_value):
   if currency_value < 0:
     raise ValueError("Currency can't be negative")
   print ('inside setter method')
   self._currency_x = currency_value

 currency_x = property(get_currency_x, set_currency_x)

c = CurrencyConverter(2)
v = c.get_currency_x()
print(v)
#print(c.__currency_x)##This call will fail.
print(c._CurrencyConverter__currency_x)##This call will fail.
