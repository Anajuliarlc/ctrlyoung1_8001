"""numero = int(input("Digite um numero: "))

if numero > 10:
    print("Maior que 10")
elif numero == 10:
    print("igual 10")
else: 
    print("menor que 10")

idade = int(input("Digite uma idade: "))

if idade >= 18:
    print("maior que 18")
else:
    print("menor")

numero = int(input("Digite um numero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("multiplo dos dois")
else:
    print("não é")

for numero in range(0,11,2):
    print(numero)"""

numero = int(input("Digite um numero: "))
contador = 0

while contador <= numero:
    print(contador)
    contador += 1