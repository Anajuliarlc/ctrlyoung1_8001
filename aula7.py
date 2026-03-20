def mensagem():
    print("Olá, mundo!")

mensagem()

def saudacao(nome):
    print("Olá, ", nome)

saudacao("Ana")

def dobro(numero):
    resultado = numero * 2
    return resultado

print(dobro(8))

def soma(n1, n2, n3):
    resultado = n1 + n2 + n3
    return resultado

#print(soma(2, 6))

def media(n1, n2, n3):
    resultado = soma(n1, n2, n3)/3
    return resultado

print(media(1, 2, 3))

def somatorio(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(somatorio(1, 5, 7))
print(somatorio(1, 5, 7, 14, 15))

def par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print(par_impar(64))
print(par_impar(33))