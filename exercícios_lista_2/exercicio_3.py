"""
3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.
"""
x: int = int(input('Digite um número: '))
if x%2 == 0:
    print(f'Número {x} é par.')
else:
    print(f'Número {x} é impar.')