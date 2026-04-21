# Seção 2 - Introdução à linguagem Python
    ## Aula 5 - O que vamos aprender nesta seção?
        como escrever códigos bonitos e interessantes

    ## Aula 6 - PEP8 - Boas práticas
        PEP (python enhancemente proposals): propostas de melhoramento do python
        o objetivo da pep 8 é permitir que escrevamos códigos de forma pythonica, ou seja, agradável
        1 - utilize camel case para nomes de classes. Criar classes com primeira letra maiúscula, se tiver mais de uma palavra no nome da classe, ambas com letra maiúscula e sem espaço entre elas
        2 - utiliza nomes em minúsculo, separadas por underline para funções e variáveis
        3 - utilize quatro espaços para identação (importante!), não é recomendado utilizar o tab
        a linguagem python é dependente de identação 
        4 - linhas em branco, entre classes, ou antes de uma classe, tem que deixar duas linhas em branco. Separar funções e definições de classe com duas linhas em branco. Métodos dentro de uma classe devem ser separados com uma única linha em branco
        5 - imports (de pacotes completos) deve ser sempre feitos em linhas separadas, exemplo:
            #import errado: 
                import sys, os
            #import correto:
                import sys
                import os
            imports devem ser colocado no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes de constantes ou variáveis globais
        6 - espaços em expressões e instruções
        7 - termine sempre uma instrução com uma nova linha
        comentários de várias linhas abre e finaliza com três aspas duplas ou três aspas simples, comentário de uma linha, utilizar cerquilha      
        
    ## Aula 7 - Dir e Help
        utilitário pythin para auxiliar na programação
        dir -  apresenta todos os atributos e funções/métodos disponíveis para determinado tipo de dado ou variável
        dir(tipo de dado/variável)
        se eu colocar uma String, ele vai me retornar todos os atributos, funções e métodos que podem usar com a string
        help - apresenta a documentação/como utilizar os atributos/propriedades e funções/métodos disponíveis para determinado tipo de dado ou variável
        help(tipo de dado/variável.propriedade)
        help("Gekk".lower)
        vai retornar a descrição do que a função lower vai fazer com a variável

    ## Aula 8 - Recebendo dados do usuário
        cast é a conversão de um tipo de dado para outro
        entrada de dados 
        (input - todo dado recebido é do tipo String)
        nome = input('Qual o seu nome?')
        print(f'Seja bem-vindo(a){nome}')
        idade = input('Qual sua idade?')
        processamento
        saída de dados
        print(f'A {nome} tem {idade} anos.')
        print(f'A {nome} nasceu em {2026 - int(idade)}')
        
        em python, string é tudo que estiver entre:
        - aspas simples;
        - aspas duplas;
        - aspas simples triplas;
        - aspas duplas triplas.

    ## Aula 9 - Recapitulando
        