def soma():
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    print("Soma: ", a + b)


def subtracao():
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    print("Subtracao: ", a - b)


def multiplicacao():
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    print("Multiplicacao: ", a * b)


def divisao():
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    print("Divisao: ", a / b)

opcao = 1

while opcao:

    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")
    print("5. Sair")

    opcao = int(input("Opção: "))

    if 1 == opcao:
        soma()
    if 2 == opcao:
        subtracao()
    if 3 == opcao:
        multiplicacao()
    if 4 == opcao:
        divisao()
