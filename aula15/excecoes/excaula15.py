"""try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    resultado = n1 / n2
except ValueError:
    print("Erro: você precisa digitar apenas números inteiros.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
else:
    print(f"Resultado: {resultado}")"""

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    print("Encerrando operação...")
    if 'arquivo' in locals():
        arquivo.close()