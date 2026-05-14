while True:
    print(f"\nSua lista: {lista_compras}")
    print("1 - Adicionar | 2 - Remover | 3 - Ver Lista | 4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("O que deseja adicionar? ")
        lista_compras.append(item)
    elif opcao == "2":
        item = input("O que deseja remover? ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"{item} removido!")
        else:
            print("Item não encontrado.")
    elif opcao == "3":
        print("\n--- Itens na Lista ---")
        for i in lista_compras:
            print(f"- {i}")
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")
