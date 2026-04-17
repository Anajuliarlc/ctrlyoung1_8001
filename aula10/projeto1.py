def mostrar_menu():
    print("\n ---MENU---")
    print("1 - Cadastrar pessoa")
    print("2 - Mostrar todos os cadastros")
    print("3 - Buscar pessoa pelo nome")
    print("4 - Remover cadastro")
    print("5 - Editar cadastro")
    print("6 - Sair")

def cadastrar_pessoa():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    cidade = input("Digite a cidade natal: ")
    email = input("Digite seu email:")

    cadastro = {
        "nome": nome,
        "idade": idade,
        "cidade_natal": cidade,
        "email": email
    }

    return cadastro

def mostrar_cadastros(cadastros):
    if len(cadastros) == 0:
        print("Nenhum cadastro encontrado.")
        return
    
    print("\n--- TODOS OS CADASTROS ---")

    for pessoa in cadastros:
        print("Nome: ", pessoa["nome"])
        print("Idade: ", pessoa["idade"])
        print("Cidade Natal: ", pessoa["cidade_natal"])
        print("Email: ", pessoa["email"])
        print("----------------------")

def buscar_pessoa(cadastros):
    if len(cadastros) == 0:
        print("Nenhum cadastro encontrado.")
        return
    
    nome_busca = input("Digite o nome da pessoa: ")

    for pessoa in cadastros:
        if pessoa["nome"].lower() == nome_busca.lower():
            print("\n--- CADASTRO ENCONTRADO ---")
            print("Nome: ", pessoa["nome"])
            print("Idade: ", pessoa["idade"])
            print("Cidade Natal: ", pessoa["cidade_natal"])
            print("Email: ", pessoa["email"])
            return
        
    print("Pessoa não encontrada.")

def remover_cadastro(cadastros):
    if len(cadastros) == 0:
        print("Nenhum cadastro encontrado.")
        return
    
    nome_remover = input("Digite o nome da pessoa que deseja remover: ")

    for index, pessoa in enumerate(cadastros):
        if pessoa["nome"].lower() == nome_remover.lower():
            print("\n--- CADASTRO REMOVIDO ---")
            print("Nome: ", pessoa["nome"])
            print("Idade: ", pessoa["idade"])
            print("Cidade Natal: ", pessoa["cidade_natal"])
            print("Email: ", pessoa["email"])
            
            cadastros.pop(index)
            return
        
    print("Pessoa não encontrada.")

def editar_cadastro(cadastros):
    if len(cadastros) == 0:
        print("Nenhum cadastro encontrado.")
        return

    nome_editar = input("Digite o nome da pessoa que deseja editar: ")

    for pessoa in cadastros:
        if pessoa["nome"].lower() == nome_editar.lower():
            print("\n--- CADASTRO ATUAL ---")
            print("Nome: ", pessoa["nome"])
            print("Idade: ", pessoa["idade"])
            print("Cidade Natal: ", pessoa["cidade_natal"])
            print("Email: ", pessoa["email"])

            novo_nome = input("Digite o novo nome: ")
            nova_idade = int(input("Digite a nova idade: "))
            nova_cidade = input("Digite a nova cidade natal: ")
            novo_email = input("Digite seu novo email:")

            pessoa["nome"] = novo_nome
            pessoa["idade"] = nova_idade
            pessoa["cidade_natal"] = nova_cidade
            pessoa["email"] = novo_email

            print("Cadastro editado com sucesso!")
            return
    
    print("Pessoa não encontrada.")


def main():
    cadastros = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pessoa = cadastrar_pessoa()
            cadastros.append(pessoa)
            print("Cadastro realizado com sucesso!")

        elif opcao == "2":
            mostrar_cadastros(cadastros)

        elif opcao == "3":
            buscar_pessoa(cadastros)

        elif opcao == "4":
            remover_cadastro(cadastros)

        elif opcao == "5":
            editar_cadastro(cadastros)

        elif opcao == "6":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()