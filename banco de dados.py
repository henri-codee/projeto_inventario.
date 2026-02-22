import sqlite3

# 1. Conectar ao banco (se não existir, ele cria o arquivo automaticamente)
conexao = sqlite3.connect('inventario.db')
cursor = conexao.cursor()

# 2. Criar a tabela com as colunas que você definiu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS estoque (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        categoria TEXT NOT NULL
    )
''')

# 3. Salvar e fechar
conexao.commit()
conexao.close()

print("Banco de dados e tabela criados com sucesso!")