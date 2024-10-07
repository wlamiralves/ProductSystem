import tkinter as tk
from tkinter import messagebox
from database import criar_banco, adicionar_produto, buscar_produto, listar_produtos, remover_produto, alterar_produto

class App:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Gerenciamento de Produtos")
        master.configure(bg="#2C3E50")  # Cor de fundo

        self.label = tk.Label(master, text="Sistema de Produtos", font=("Helvetica", 18), bg="#2C3E50", fg="#ECF0F1")
        self.label.pack(pady=10)

        # Frame para adicionar produtos
        self.frame_adicionar = tk.Frame(master, bg="#34495E")
        self.frame_adicionar.pack(pady=10)

        self.nome_label = tk.Label(self.frame_adicionar, text="Nome do Produto:", bg="#34495E", fg="#ECF0F1")
        self.nome_label.grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.frame_adicionar)
        self.nome_entry.grid(row=0, column=1)

        self.quantidade_label = tk.Label(self.frame_adicionar, text="Quantidade:", bg="#34495E", fg="#ECF0F1")
        self.quantidade_label.grid(row=1, column=0)
        self.quantidade_entry = tk.Entry(self.frame_adicionar)
        self.quantidade_entry.grid(row=1, column=1)

        self.adicionar_button = tk.Button(self.frame_adicionar, text="Adicionar Produto", command=self.adicionar_produto, bg="#27AE60", fg="#FFFFFF")
        self.adicionar_button.grid(row=2, columnspan=2)

        # Frame para buscar produtos
        self.frame_buscar = tk.Frame(master, bg="#34495E")
        self.frame_buscar.pack(pady=10)

        self.buscar_label = tk.Label(self.frame_buscar, text="Buscar Produto:", bg="#34495E", fg="#ECF0F1")
        self.buscar_label.grid(row=0, column=0)
        self.buscar_entry = tk.Entry(self.frame_buscar)
        self.buscar_entry.grid(row=0, column=1)

        self.buscar_button = tk.Button(self.frame_buscar, text="Buscar", command=self.buscar_produto, bg="#2980B9", fg="#FFFFFF")
        self.buscar_button.grid(row=0, column=2)

        # Frame para remover produtos
        self.frame_remover = tk.Frame(master, bg="#34495E")
        self.frame_remover.pack(pady=10)

        self.remover_label = tk.Label(self.frame_remover, text="ID do Produto a Remover:", bg="#34495E", fg="#ECF0F1")
        self.remover_label.grid(row=0, column=0)
        self.remover_entry = tk.Entry(self.frame_remover)
        self.remover_entry.grid(row=0, column=1)

        self.remover_button = tk.Button(self.frame_remover, text="Remover Produto", command=self.remover_produto, bg="#C0392B", fg="#FFFFFF")
        self.remover_button.grid(row=0, column=2)

        # Frame para alterar produtos
        self.frame_alterar = tk.Frame(master, bg="#34495E")
        self.frame_alterar.pack(pady=10)

        self.alterar_label = tk.Label(self.frame_alterar, text="ID do Produto a Alterar:", bg="#34495E", fg="#ECF0F1")
        self.alterar_label.grid(row=0, column=0)
        self.alterar_entry = tk.Entry(self.frame_alterar)
        self.alterar_entry.grid(row=0, column=1)

        self.novo_nome_label = tk.Label(self.frame_alterar, text="Novo Nome:", bg="#34495E", fg="#ECF0F1")
        self.novo_nome_label.grid(row=1, column=0)
        self.novo_nome_entry = tk.Entry(self.frame_alterar)
        self.novo_nome_entry.grid(row=1, column=1)

        self.nova_quantidade_label = tk.Label(self.frame_alterar, text="Nova Quantidade:", bg="#34495E", fg="#ECF0F1")
        self.nova_quantidade_label.grid(row=2, column=0)
        self.nova_quantidade_entry = tk.Entry(self.frame_alterar)
        self.nova_quantidade_entry.grid(row=2, column=1)

        self.alterar_button = tk.Button(self.frame_alterar, text="Alterar Produto", command=self.alterar_produto, bg="#F39C12", fg="#FFFFFF")
        self.alterar_button.grid(row=3, columnspan=2)

        # Botão para listar todos os produtos
        self.listar_button = tk.Button(master, text="Listar Todos os Produtos", command=self.listar_produtos, bg="#8E44AD", fg="#FFFFFF")
        self.listar_button.pack(pady=10)

        # Área de texto para resultados
        self.resultado_text = tk.Text(master, height=20, width=70, bg="#ECF0F1", fg="#2C3E50", font=("Helvetica", 12))
        self.resultado_text.pack(pady=10)

        criar_banco()

    def adicionar_produto(self):
        nome = self.nome_entry.get()
        quantidade = self.quantidade_entry.get()
        
        if nome and quantidade.isdigit():
            adicionar_produto(nome, int(quantidade))
            messagebox.showinfo("Sucesso", "Produto adicionado.")
            self.nome_entry.delete(0, tk.END)
            self.quantidade_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Insira nome e quantidade válidos.")

    def buscar_produto(self):
        nome = self.buscar_entry.get()
        if nome:
            produtos = buscar_produto(nome)
            self.resultado_text.delete(1.0, tk.END)
            if produtos:
                for produto in produtos:
                    self.resultado_text.insert(tk.END, f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}\n")
            else:
                self.resultado_text.insert(tk.END, "Produto não encontrado.")
        else:
            messagebox.showerror("Erro", "Insira um nome válido.")

    def listar_produtos(self):
        produtos = listar_produtos()
        self.resultado_text.delete(1.0, tk.END)
        if produtos:
            for produto in produtos:
                self.resultado_text.insert(tk.END, f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}\n")
        else:
            self.resultado_text.insert(tk.END, "Nenhum produto cadastrado.")

    def remover_produto(self):
        produto_id = self.remover_entry.get()
        if produto_id.isdigit():
            remover_produto(int(produto_id))
            messagebox.showinfo("Sucesso", "Produto removido.")
            self.remover_entry.delete(0, tk.END)
            self.listar_produtos()  # Atualiza a lista de produtos
        else:
            messagebox.showerror("Erro", "Insira um ID válido.")

    def alterar_produto(self):
        produto_id = self.alterar_entry.get()
        novo_nome = self.novo_nome_entry.get()
        nova_quantidade = self.nova_quantidade_entry.get()
        
        if produto_id.isdigit() and novo_nome and nova_quantidade.isdigit():
            alterar_produto(int(produto_id), novo_nome, int(nova_quantidade))
            messagebox.showinfo("Sucesso", "Produto alterado.")
            self.alterar_entry.delete(0, tk.END)
            self.novo_nome_entry.delete(0, tk.END)
            self.nova_quantidade_entry.delete(0, tk.END)
            self.listar_produtos()  # Atualiza a lista de produtos
        else:
            messagebox.showerror("Erro", "Insira dados válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
