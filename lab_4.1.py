#Исламов    
#Вариант 8, задача 4.1

print((lambda n, z: __import__("functools").reduce(__import__("operator").mul, filter(lambda x: x % z == 0, map(int, str(n))), 1))(*map(int, input().split())))