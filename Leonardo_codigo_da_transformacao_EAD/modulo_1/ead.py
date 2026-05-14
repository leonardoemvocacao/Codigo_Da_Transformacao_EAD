num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da opção (1/2/3/4): ")


if opcao == '1':
    resultado = num1 + num2
    print("O resultado da soma é:", resultado)

elif opcao == '2':
    resultado = num1 - num2
    print("O resultado da subtração é:", resultado)

elif opcao == '3':
    resultado = num1 * num2
    print("O resultado da multiplicação é:", resultado)

elif opcao == '4':
    if num2 != 0:
        resultado = num1 / num2
        print("O resultado da divisão é:", resultado)
    else:
        print("Erro! Não dá para dividir por zero.")

else:
    print("Opção inválida!")

print("Fim do programa!")
