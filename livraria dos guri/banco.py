import sqlite3

def conectar_banco():
    return sqlite3.connect('data/livraria.db')

def criar_tabela():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            ano_publicacao INTEGER,
            preco REAL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_livro():
    conn = conectar_banco()
    cursor = conn.cursor()
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano_publicacao = int(input("Ano de publicação: "))
    preco = float(input("Preço: "))
    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano_publicacao, preco)
        VALUES (?, ?, ?, ?)
    ''', (titulo, autor, ano_publicacao, preco))
    conn.commit()
    conn.close()

def exibir_livros():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    for livro in livros:
        print(livro)
    conn.close()

def atualizar_preco_livro():
    conn = conectar_banco()
    cursor = conn.cursor()
    id_livro = int(input("ID do livro a ser atualizado: "))
    novo_preco = float(input("Novo preço: "))
    cursor.execute('''
        UPDATE livros
        SET preco = ?
        WHERE id = ?
    ''', (novo_preco, id_livro))
    conn.commit()
    conn.close()

def remover_livro():
    conn = conectar_banco()
    cursor = conn.cursor()
    id_livro = int(input("ID do livro a ser removido: "))
    cursor.execute('DELETE FROM livros WHERE id = ?', (id_livro,))
    conn.commit()
    conn.close()

def buscar_livros_por_autor():
    conn = conectar_banco()
    cursor = conn.cursor()
    autor = input("Autor: ")
    cursor.execute('SELECT * FROM livros WHERE autor LIKE ?', ('%' + autor + '%',))
    livros = cursor.fetchall()
    for livro in livros:
        print(livro)
    conn.close()
