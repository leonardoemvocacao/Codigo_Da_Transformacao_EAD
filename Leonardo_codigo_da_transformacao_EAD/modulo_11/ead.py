
print("--- CALCULADORA ---")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print("A soma é:", soma)
print("A subtração é:", subtracao)
print("A multiplicação é:", multiplicacao)
print("A divisão é:", divisao)

print("\n---------------------------\n")

# --- Atividade 2: Ver qual número é maior ---
print("--- QUAL É O MAIOR? ---")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print("O primeiro número é maior!")
elif n2 > n1:
    print("O segundo número é maior!")
else:
    print("Os números são iguais!")

print("\n---------------------------\n")

# --- Atividade 3: Classificar Idade ---
print("--- CLASSIFICADOR DE IDADE ---")
idade = int(input("Quantos anos você tem? "))

if idade <= 12:
    print("Você é uma Criança")
elif idade >= 13 and idade <= 17:
    print("Você é um Adolescente")
elif idade >= 18 and idade <= 59:
    print("Você é um Adulto")
else:
    print("Você é um Idoso")

print("\n---------------------------\n")

# --- Desafio Extra: Menu com While ---
print("--- AGORA VAMOS TESTAR O MENU (WHILE) ---")

continuar = "sim"

while continuar == "sim":
    print("O que você quer fazer?")
    print("A - Somar")
    print("B - Sair")
    
    escolha = input("Digite A ou B: ")
    
    if escolha == "A" or escolha == "a":
        v1 = float(input("Número 1: "))
        v2 = float(input("Número 2: "))
        print("Resultado:", v1 + v2)
    elif escolha == "B" or escolha == "b":
        print("Saindo do programa...")
        continuar = "não" # Isso faz o while parar
    else:
        print("Opção errada!")
