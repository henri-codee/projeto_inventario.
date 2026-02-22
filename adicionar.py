import sqlite3

def adicionar_item():
    # 1. Coletar dados do usuário (Lógica de Programação)
    nome = input("Digite o nome do item: ")
    quantidade = int(input("Digite a quantidade: "))
    categoria = input("Digite a categoria: ")

    # 2. Conectar ao banco
    conexao = sqlite3.connect('inventario.db')
    cursor = conexao.cursor()

    # 3. Comando SQL para inserir (Banco de Dados)
    cursor.execute("INSERT INTO estoque (nome, quantidade, categoria) VALUES (?, ?, ?)", 
                   (nome, quantidade, categoria))

    # 4. Salvar e fechar
    conexao.commit()
    conexao.close()
    print(f"Sucesso! {nome} foi adicionado ao bunker.")

# Executar a função
adicionar_item()