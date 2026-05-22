import sqlite3


conexao = sqlite3.connect("clientes.db")


cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

print("Tabela criada com sucesso!")



def inserir_cliente(nome, email):
    cursor.execute("""
    INSERT INTO clientes (nome, email)
    VALUES (?, ?)
    """, (nome, email))

    conexao.commit()
    print("Cliente inserido com sucesso!")


def listar_clientes():
    cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    print("\n--- LISTA DE CLIENTES ---")

    for cliente in clientes:
        print(cliente)




def atualizar_cliente(id, novo_nome, novo_email):
    cursor.execute("""
    UPDATE clientes
    SET nome = ?, email = ?
    WHERE id = ?
    """, (novo_nome, novo_email, id))

    conexao.commit()
    print("Cliente atualizado!")



def deletar_cliente(id):
    cursor.execute("""
    DELETE FROM clientes
    WHERE id = ?
    """, (id,))

    conexao.commit()
    print("Cliente deletado!")



def clientes_com_a():
    cursor.execute("""
    SELECT * FROM clientes
    WHERE nome LIKE 'A%'
    """)

    resultado = cursor.fetchall()

    print("\n--- CLIENTES COM A ---")

    for cliente in resultado:
        print(cliente)


inserir_cliente("Ana", "ana@gmail.com")
inserir_cliente("Carlos", "carlos@gmail.com")
inserir_cliente("Amanda", "amanda@gmail.com")

listar_clientes()

atualizar_cliente(1, "Ana Clara", "anaclara@gmail.com")

listar_clientes()

clientes_com_a()

deletar_cliente(2)

listar_clientes()

conexao.close()
