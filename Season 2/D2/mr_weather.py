from random import randint
x = randint (0, 100)

sunny = '''    |
  \ | /
   \*/
--**O**-- 
   /*/
  / | /
    |
'''
cloudy = '''          .-~~~-.
  .- ~ ~-(       )_ _
 /                     ~ -.
|                           |
 \                         .'
   ~- . _____________ . -~'''
rainy = '''
    _(  )_( )_
   (_   _    _)
  / /(_) (__)
 / / / / / /
/ / / / / /'''
print(x)
if x<30:
    print("Rainy.")
    print(rainy)
elif x<60:
    print("Cloudy.")
    print(cloudy)
else:
    print("Sunny.")
    print(sunny)