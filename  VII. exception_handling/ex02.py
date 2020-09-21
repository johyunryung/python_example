class MyError(Exception):
  def __init__(self,message):
     self.message = message
  def __str__(self):
     return self.message

class NotEvenNumberError(Exception):
   def __init__(self):
      pass
   def __str__(self):
      return "짝수가 아니어라"

def even_number_add(a,b):
   if a % 2 != 0 or b % 2 != 0:
      raise NotEvenNumberError
   return a + b

try:
   a = even_number_add(2,2)
   print(a)
   b = even_number_add(4,2)
   print(b)
   c = even_number_add(2,1)
   print(c)
except NotEvenNumberError as e:
   print(e)
