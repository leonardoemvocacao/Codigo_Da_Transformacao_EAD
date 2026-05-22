import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)



def inicializar_banco():
  
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """
    )

    conexao.commit()
    conexao.close()



inicializar_banco()



@app.route("/saudacao", methods=["GET"])
def saudacao():
    return (
        jsonify({"mensagem": "Olá! Seja muito bem-vindo à nossa API Flask!"}),
        200,
    )



@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    dados = request.get_json()


    if not dados or "nome" not in dados or "email" not in dados:
        return (
            jsonify({"erro": "Por favor, envie os campos 'nome' e 'email'."}),
            400,
        )

    nome_usuario = dados["nome"]
    email_usuario = dados["email"]


    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()


    cursor.execute(
        "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
        (nome_usuario, email_usuario),
    )

    conexao.commit()
    conexao.close()

 
    return (
        jsonify(
            {
                "mensagem": "Usuário cadastrado com sucesso!",
                "usuario": {"nome": nome_usuario, "email": email_usuario},
            }
        ),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True)
