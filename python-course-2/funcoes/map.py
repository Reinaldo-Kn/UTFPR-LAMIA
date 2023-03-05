#!python3
from functools import reduce

def somar_nota(delta):
    def calc(nota):
        return nota + 1.5
    return calc

def somar(a,b):
    return a+b
notas = [5.3, 7.2, 3.1, 4.0]
finais = map(somar_nota(1),notas)

total = reduce(somar,notas,0)
print(total)