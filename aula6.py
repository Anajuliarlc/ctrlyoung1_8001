"""cores = ("amarelo", "verde", "azul")
print(cores[0])

numeros = (2, 25, 4, 8, 9, 258, 67, 9, 6)
tamanho = len(numeros)
print(tamanho)

tupla = (1,2,2,3,2)
print(tupla.count(2))

tupla2 = (10,20,30,40)
print(tupla2.index(30))

numeros2 = {1, 2, 3, 3, 4, 4}
print(numeros2)

set_vazio = set()
set_vazio.add(10)
set_vazio.add(20)
set_vazio.add(30)
print(set_vazio)

frutas = {"uva", "maça", "morango"}
for fruta in frutas:
    print(fruta)

numeros = {1,2,3,4,5}
divisao = 6/2
print(divisao)
print(5 in numeros)
print(divisao in numeros)"""

aluno = {
    "nome" : "Ana",
    "idade": 23,
    "curso": "Python"
}

print(aluno)
print(aluno["nome"])

aluno["cidade"] = "Vila Velha"
print(aluno)

print(aluno.keys())
print(aluno.values())
print(aluno.items())