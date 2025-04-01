print("Menu de opções:")
print("1. Adicionar informações")
print("2. Consultar informações")
print("3. Sair")

while True:
    escolha = input("Escolha uma opção (1, 2, 3): ")

    if escolha == "1":
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        idade = input("Digite a idade: ")

        # Salvando as informações no arquivo lista.txt
        with open("lista.txt", "a") as arquivo:
            arquivo.write(f"{nome},{sobrenome},{idade}\n")
        print("Informações adicionadas com sucesso!")

    elif escolha == "2":
        try:
            with open("lista.txt", "r") as arquivo:
                conteudo = arquivo.readlines()

            if conteudo:
                for linha in conteudo:
                    print(linha.strip())
            else:
                print("Nenhuma informação cadastrada.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    elif escolha == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")