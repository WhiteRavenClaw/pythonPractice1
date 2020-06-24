from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.GREEN)
what = (input('Привет тебе и увлекательной математике!\nЧто нужно:+, -, *,/?  '))
print(Back.CYAN)
x=float(input("ВВеди 1 число  "))
y=float(input("ВВеди 2 число  "))
print(Back.YELLOW)
if what == '+':
    z = x+y
    print('Рез: ' + str(z))
elif what == "-":
    z = x-y
    print('Рез: ' + str(z))
elif what == "*":
    z = x*y
    print('Рез: ' + str(z))
else:
    z = x/y
    print('Рез: ' + str(z))
input()
