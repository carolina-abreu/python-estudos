"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""

x: int = int(input('Digite um número inteiro qualquer: '))
y: int = int(input('Digite outro número inteiro qualquer: '))

if x > y:
    print(f'Número {x} é maior que {y}.')
elif x < y:
    print(f'Número {y} é maior que {x}.')
else:
    print(f'Número {x} é igual a {y}.')