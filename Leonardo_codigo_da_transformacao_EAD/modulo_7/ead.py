def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    else:
        return a / b



import calculadora

print("===================================")
print("     CALCULADORA EM PYTHON")
print("===================================")

# Pedindo os números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Menu
print("\nEscolha uma operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Digite a opção: ")

# Verificando a opção escolhida
if opcao == "1":
    resultado = calculadora.somar(numero1, numero2)
    print("Resultado da soma:", resultado)

elif opcao == "2":
    resultado = calculadora.subtrair(numero1, numero2)
    print("Resultado da subtração:", resultado)

elif opcao == "3":
    resultado = calculadora.multiplicar(numero1, numero2)
    print("Resultado da multiplicação:", resultado)

elif opcao == "4":
    resultado = calculadora.dividir(numero1, numero2)
    print("Resultado da divisão:", resultado)

else:
    print("Opção inválida")

print("\nPrograma finalizado.")
