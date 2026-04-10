"""import math as m
import utilidades as utilidades
from calculos import soma
import meu_pacote.operacoes as op
#import utilidades as u
#from utilidades import saudacao
#from math import factorial, pow
import os

#os.remove("teste.txt")
#os.rmdir("aleatoria")

print(m.pow(2, 3))
print(m.factorial(5))
print(m.ceil(4.2))
print(m.trunc(4.9))
print(dir(m))

utilidades.saudacao("Ana")
#u.saudacao("Ana")
#saudacao("Daniel")

print(soma(51, 9))
print(op.dobro(9))

#Faça um programa que leia 5 valores inteiros. 
#Conte quantos destes valores digitados são pares e mostre esta informação.

contador_pares = 0

for n in range(5):
    numero = int(input("Digite um numero: "))

    if numero % 2 == 0:
        contador_pares += 1

print("Quantidade de numeros pares:", contador_pares)"""

#Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos 
# a partir de X, um valor por linha, inclusive o X se for o caso

numero = int(input("Digite um número: "))
contador = 0

while contador < 6:
    if numero % 2 != 0:
        print(numero)
        contador += 1
    numero += 1
