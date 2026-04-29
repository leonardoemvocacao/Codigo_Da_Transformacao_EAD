def exibir_menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Mostrar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

def main():
    tarefas = []
    
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-4): ")

        if escolha == '1':
            nova_tarefa = input("Digite a tarefa: ")
            tarefas.append(nova_tarefa)
            print("Tarefa adicionada com sucesso!")
        
        elif escolha == '2':
            print("\nSua Lista de Tarefas:")
            if not tarefas:
                print("A lista está vazia.")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. {tarefa}")
        
        elif escolha == '3':
            if not tarefas:
                print("Nada para remover.")
                continue
            
            try:
                indice = int(input("Digite o número da tarefa para remover: ")) - 1
                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    print(f"Tarefa '{removida}' removida!")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")
        
        elif escolha == '4':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
