def calculadora(num1, num2, operacao):
    num1 = float(input("Qual o primeiro número?"))
    num2 = float(input("Qual o segundo número?"))
    operacao = int(input("Qual a operação? 1.Soma,2.Subtração,3.Multiplicação,4.Divisão "))

    if operacao == 1:
        print(num1 + num2)
    elif operacao == 2:
        print(num1 - num2)
    elif operacao == 3:
        print(num1 * num2)
    elif operacao == 4:
        print(num1 / num2)
    else:
        print(0)

calculadora(0,0,0)