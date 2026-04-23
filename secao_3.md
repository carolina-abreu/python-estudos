# Seção 3 - Variáveis e Tipos de Dados em Python
    ## Aula 10 - O que vamos aprender nesta seção?
        variáveis

    ## Aula 11 - O tipo numérico
        -5/2 = 2.5
        -5//2 = 2 (duas barras dá um número inteiro)
        -4%2 = 0 (resto da divisão)
        -7%2 = 1 (resto da divisão)
        -2**8 = 256 (2 elevado 8)
        -1_000_000_000 = posso colocar as unidades entre _, que o python entende oq quero dizer, 1milhão
        - num = 42
        num.__add__(8) = 50

    ## Aula 12 - O tipo float
        tipo real, decimal
        com casas decimais
        o separador de casa decimal é . e não ,
        número complexo em python é representado por j, ou seja, variável = 5j
        5j é do tipo complexa
        é possível converter float para inteiro, mas perde precisão

    ## Aula 13 - O tipo boleano
        vem da algebra booleana criada por George Boole
        tem duas contantes: verdadeiro ou falso
        em python:
        True - Verdadeiro
        False - Falso 
        sempre com a incial maiúscula
        utiliza para operações básicas 
        - negação (not): fazendo a negação, se o valor booleano for verdadeiro o resultado é falso, se for falso o resultado será verdadeiro, ou seja, sempre ao contrário
        - ou (or): é uma operaçao binária, ou seja, depende de dois valores, ou um ou outro deve ser verdadeiro. Exemplo:
        True or True = True
        True or False = True
        False or True = True
        False or False = False (pq não tem nenhum valor verdadeiro)
        - e (and): é uma operação binária, ou seja, depende de dois valores, ambos devem ser verdadeiro. Exemplo:
        True and True = True
        True and False = False
        False and True = False
        False and False = False

    ## Aula 14 - O tipo string
        em python, um dado é considerado do tipo strig sempre que tiver:
        - entre aspas simples (mais comum)
        - entre aspas duplas
        - entre aspas simples triplas
        - entre aspas duplas triplas
        nome = 'Carolina \nAbreu'
        print {nome} 
        Carolina
        Abreu (o \n quebra linha)
        -slice de tring
        nome = 'Geek University'
        print{nome[0:4]} imprime Geek
        print{nome[5:15]} imprime University
        print{nome.split()[0]} imprime Geek
        print{nome.split()[1]} imprime University
        print {nome[::-1]} imprime Geek University invertido (ytisrevinU keeG)
        print{nome.replace['G','P']} imprime Peek University

    ## Aula 15 - Escopo de variáveis
        - variáveis globais: são reconhecidas, ou seia, seu escopo compreende, todo o programa
        - variáveis locais: são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarada
        - para declarar variáveis em python fazemos:
        nome_da_variável = valor_da_variável
            

    ## Aula 16 - Exercícios
    ## Aula 17 - Recapitulando