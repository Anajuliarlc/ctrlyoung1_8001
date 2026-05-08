class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Ana", 23)
print(pessoa1.nome)
print(pessoa1.idade)

class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

carro = Carro("Toyota", "Corolla", 120)

print(carro.marca)
print(carro.modelo)
print(carro.velocidade)

class Animal:
    def emitir_som(self):
        print("O animal fez um som.")

animal = Animal()
animal.emitir_som()

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Nota:", self.nota)

aluno = Aluno("Carlos", 9)
aluno.mostrar_dados()

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado.")
        else:
            print("Saldo insuficiente.")

conta = ContaBancaria("Ana", 100)
conta.depositar(50)
print(conta.saldo)
conta.sacar(200)
conta.sacar(30)
print(conta.saldo)
