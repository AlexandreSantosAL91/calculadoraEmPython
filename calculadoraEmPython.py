"""
Criando uma calculadora utilizando a linguagem Python

O script pergunta qual operação o usuário deseja rodar
(soma, subtração, multiplicação ou divisão) e executa
a operação.
"""


def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Soma: ", x + y)


def subtracao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Subtracao: ", x - y)


def multiplicacao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Multiplicacao: ", x * y)


def divisao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Divisao: ", x / y)


opcao = 1

while opcao:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")

    opcao = int(input("Opção: "))

    if 1 == opcao:
        soma()
    if 2 == opcao:
        subtracao()
    if 3 == opcao:
        multiplicacao()
    if 4 == opcao:
        divisao()
