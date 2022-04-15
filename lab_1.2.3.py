
#islamov
#lab 1.2.3 var 8
from math import tan
from math import fabs
x, y, a, b = map(float,input('Введите(через пробел) 4 числа (x, y, a, b) = ').split())
print(f"F = {tan(((x-(1/tan(x-y)))/fabs(x**2 +a*x+b**2))):.3f}")