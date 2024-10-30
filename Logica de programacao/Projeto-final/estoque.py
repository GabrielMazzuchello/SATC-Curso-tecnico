import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para verificar os campos e cadastrar o produto
def cadastrar_produto():
    nome = nome_entry.get().strip()
    quantidade = quantidade_entry.get().strip()
    preco = preco_entry.get().strip()

    if not nome or not quantidade or not preco:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos!")
    else:
        # Aqui você pode adicionar o código para inserir os dados no banco de dados
        print(f"Produto cadastrado: {nome}, Quantidade: {quantidade}, Preço: {preco}")
        # Limpa os campos após o cadastro
        nome_entry.delete(0, tk.END)
        quantidade_entry.delete(0, tk.END)
        preco_entry.delete(0, tk.END)


# Criação da janela principal
root = tk.Tk()
root.title("Gerenciador de Estoque")
root.geometry("800x500")

# Frame para Formulário de Entrada
form_frame = tk.Frame(root, padx=10, pady=10)
form_frame.pack(side=tk.TOP, fill=tk.X)

# Labels e Entradas do Formulário
tk.Label(form_frame, text="Nome do Produto:").grid(row=0, column=0, padx=5, pady=5)
nome_entry = tk.Entry(form_frame)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Quantidade:").grid(row=0, column=2, padx=5, pady=5)
quantidade_entry = tk.Entry(form_frame)
quantidade_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(form_frame, text="Preço:").grid(row=1, column=0, padx=5, pady=5)
preco_entry = tk.Entry(form_frame)
preco_entry.grid(row=1, column=1, padx=5, pady=5)

# Botões de Ação
button_frame = tk.Frame(root, pady=10)
button_frame.pack(side=tk.TOP, fill=tk.X)

tk.Button(button_frame, text="Adicionar", command=cadastrar_produto, width=12).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Atualizar", width=12).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Excluir", width=12).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Pesquisar", width=12).pack(side=tk.LEFT, padx=10)

# Tabela de Produtos
table_frame = tk.Frame(root, pady=10)
table_frame.pack(fill=tk.BOTH, expand=True)

columns = ("ID", "Nome", "Quantidade", "Preço")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER, width=100)

tree.pack(fill=tk.BOTH, expand=True)

# Execução da interface
root.mainloop()
