
with open('lista_compras.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Arroz\n')
    arquivo.write('Feijão\n')
    arquivo.write('Ovos\n')

print("Arquivo TXT criado com sucesso!")


with open('lista_compras.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo da lista:")
    print(conteudo)
