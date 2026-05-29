"""try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    resultado = n1 / n2

except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")

except ValueError:
    print("Erro: digite apenas números.")

else:
    print("Resultado:", resultado)

try:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

except ValueError:
    print("Erro: entrada inválida.")"""

#nivel 2 act 1

try:
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        raise ValueError("Idade não pode ser negativa.")

    print("Idade válida.")

except ValueError as erro:
    print("Erro:", erro)