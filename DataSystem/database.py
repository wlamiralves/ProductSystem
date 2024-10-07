import sqlite3
import os

def criar_banco():
    if not os.path.exists('data'):
        os.makedirs('data')
    
    conexao = sqlite3.connect('data/banco_de_dados.db')
    cursor = conexao.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL
    )
    ''')
    
    conexao.commit()
    conexao.close()

def adicionar_produto(nome, quantidade):
    conexao = sqlite3.connect('data/banco_de_dados.db')
    cursor = conexao.cursor()
    
    cursor.execute('INSERT INTO produtos (nome, quantidade) VALUES (?, ?)', (nome, quantidade))
    
    conexao.commit()
    conexao.close()

def buscar_produto(nome):
    conexao = sqlite3.connect('data/banco_de_dados.db')
    cursor = conexao.cursor()
    
    cursor.execute('SELECT * FROM produtos WHERE nome LIKE ?', ('%' + nome + '%',))
    produtos = cursor.fetchall()
    
    conexao.close()
    return produtos

def listar_produtos():
    conexao = sqlite3.connect('data/banco_de_dados.db')
    cursor = conexao.cursor()
    
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    
    conexao.close()
    return produtos

def remover_produto(produto_id):
    conexao = sqlite3.connect('data/banco_de_dados.db')
    cursor = conexao.cursor()
    
    cursor.execute('DELETE FROM produtos WHERE id = ?', (produto_id,))
    
    conexao.commit()
    conexao.close()

def alterar_produto(produto_id, novo_nome, nova_quantidade):
    conexao = sqlite3.connect('data/banco_de_dados.db')
    cursor = conexao.cursor()
    
    cursor.execute('UPDATE produtos SET nome = ?, quantidade = ? WHERE id = ?', (novo_nome, nova_quantidade, produto_id))
    
    conexao.commit()
    conexao.close()
