#lab 3.1 
#var 8 Islamov

d,t = map(int, input('Введите (через пробел) 2 числа (d,t) = ').split())
print(f"P = {(max(min(d, 7), min(t, 7)) / 7):.3f}")
