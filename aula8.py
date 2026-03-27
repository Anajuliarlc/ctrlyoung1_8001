with open("teste.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!")

with open("teste.txt", "r") as arquivo:
    print(arquivo.read())

with open("teste.txt", "w") as arquivo:
    arquivo.write("oiwqudid!\nblabla!\n")

with open("teste.txt", "r") as arquivo:
    print(arquivo.readline())

with open("teste.txt", "a") as arquivo:
    arquivo.write("Olá, mundo!")

with open("teste.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)

#Crie um programa que peça um nome e salve no arquivo.
nome = input("digite seu nome: ")

with open("teste.txt", "a") as arquivo:
    arquivo.write(nome + "\n")