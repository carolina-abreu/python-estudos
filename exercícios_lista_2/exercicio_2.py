"""
2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""
from math import sqrt

x: int = int(input('Digite um número: '))

if x > 0:
    print(f'Raiz quadrada de {x} é {sqrt(x):.2f}.')
elif x < 0:
    print(f'Número inválido.')
