usuarios_cadastrados = {
    "admin": "1234",
    "joao": "senhaSegura",
    "maria": "python123"
}

def sistema_login(usuario, senha):

    if usuario in usuarios_cadastrados:

        if usuarios_cadastrados[usuario] == senha:
            return "Login realizado com sucesso!"
        else:
            return "Senha incorreta."
    else:
        return "Usuário não encontrado."


user_input = input("Digite o usuário: ")
pass_input = input("Digite a senha: ")

status = sistema_login(user_input, pass_input)
print(status
