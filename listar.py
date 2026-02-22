import sqlite3

def listar_itens():
    # 1. Conectar ao banco
    conexao = sqlite3.connect('inventario.db')
    cursor = conexao.cursor()

    # 2. Comando SQL para buscar tudo (*) da tabela estoque
    cursor.execute("SELECT * FROM estoque")
    
    # 3. Recuperar os dados
    itens = cursor.fetchall()

    print("\n--- 📦 INVENTÁRIO DO BUNKER ---")
    if not itens:
        print("O inventário está vazio!")
    else:
        for item in itens:
            # item[0] é o ID, item[1] é o Nome, item[2] a Qtd, item[3] a Categoria
            print(f"ID: {item[0]} | Nome: {item[1]} | Qtd: {item[2]} | Cat: {item[3]}")
    
    print("-------------------------------\n")

    # 4. Fechar conexão
    conexao.close()

listar_itens()