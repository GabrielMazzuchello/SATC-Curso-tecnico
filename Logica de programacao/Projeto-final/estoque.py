import tkinter as tk
from tkinter import messagebox

def abrir_estoque():
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

    tk.Button(button_frame, text="Adicionar", width=12).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Atualizar", width=12).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Excluir", width=12).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Pesquisar", width=12).pack(side=tk.LEFT, padx=10)

    # Tabela de Produtos
    table_frame = tk.Frame(root, pady=10)
    table_frame.pack(fill=tk.BOTH, expand=True)

    columns = ("ID", "Nome", "Quantidade", "Preço")
    tree = tk.Treeview(table_frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, width=100)

    tree.pack(fill=tk.BOTH, expand=True)

    # Execução da interface
    root.mainloop()

# Funções para os botões
def entrar():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    # Lógica de autenticação (aqui apenas um exemplo)
    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        abrir_estoque()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

def registrar():
    # Lógica de registro (pode incluir cadastro no banco de dados)
    messagebox.showinfo("Registrar", "Função de registro chamada.")

# Janela principal
root = tk.Tk()
root.title("Login")
root.geometry("300x200")
root.resizable(False, False)  # Impede redimensionamento da tela

# Labels e Entradas para Usuário e Senha
tk.Label(root, text="Usuário").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entrada_usuario = tk.Entry(root)
entrada_usuario.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Senha").grid(row=3, column=0, padx=10, pady=10, sticky="e")
entrada_senha = tk.Entry(root, show="")  # show="" para esconder a senha
entrada_senha.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

# Botões Registrar e Entrar
btn_registrar = tk.Button(root, text="Registrar", command=registrar)
btn_registrar.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")

btn_entrar = tk.Button(root, text="Entrar", command=entrar)
btn_entrar.grid(row=5, column=1, columnspan=2, padx=10, pady=10, sticky="w")

# Executar a interface
root.mainloop()