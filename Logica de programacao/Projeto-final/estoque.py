import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importação do ttk para o Treeview
import mysql.connector

conexao_banco = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456789",
    database="estoque"
)

cursor = conexao_banco.cursor()

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
    nome_entry.grid(row=1, column=0, padx=5, pady=5)

    tk.Label(form_frame, text="Quantidade:").grid(row=0, column=1, padx=5, pady=5)
    quantidade_entry = tk.Entry(form_frame)
    quantidade_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Preço:").grid(row=0, column=2, padx=5, pady=5)
    preco_entry = tk.Entry(form_frame)
    preco_entry.grid(row=1, column=2, padx=5, pady=5)

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
    tree = ttk.Treeview(table_frame, columns=columns, show="headings")  # Uso de ttk.Treeview

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, width=100)

    tree.pack(fill=tk.BOTH, expand=True)

    # Execução da interface
    root.mainloop()





# Funções para verificar o usuario e a senha e abrir o sistema (algusto fazer)
def entrar():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == "admin" and senha == "123":
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        abrir_estoque()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

def registrar_novo_usuario(usuario, senha):
    if usuario and senha:
        comando = ("INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)")
        cursor.execute(comando, (usuario, senha))
        conexao_banco.commit()
        messagebox.showinfo("Registro", "Usuário registrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

def abrir_janela_cadastro():
    cadastro_window = tk.Toplevel(root)
    cadastro_window.title("Registrar Novo Usuário")
    cadastro_window.geometry("300x200")
    
    # Label e Campo para Nome de Usuário
    tk.Label(cadastro_window, text="Nome de Usuário").pack(pady=5)
    novo_usuario_entrada = tk.Entry(cadastro_window, width=30)
    novo_usuario_entrada.pack(pady=5)
    
    # Label e Campo para Senha
    tk.Label(cadastro_window, text="Senha").pack(pady=5)
    nova_senha_entrada = tk.Entry(cadastro_window, width=30, show="*")
    nova_senha_entrada.pack(pady=5)
    
    # Botão para Registrar
    tk.Button(cadastro_window, text="Registrar", command=lambda: registrar_novo_usuario(novo_usuario_entrada.get(), nova_senha_entrada.get())).pack(pady=10)





# Janela principal
root = tk.Tk()
root.title("Login")

# Definindo tamanho fixo e centralizado
window_width, window_height = 300, 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
root.resizable(False, False)

# Frame centralizado para o conteúdo de login
login_frame = tk.Frame(root, padx=20, pady=20)
login_frame.pack(expand=True)

# Labels e Entradas para Usuário e Senha
tk.Label(login_frame, text="Usuário").pack(anchor="w")
entrada_usuario = tk.Entry(login_frame, width=30)
entrada_usuario.pack(pady=5)

tk.Label(login_frame, text="Senha").pack(anchor="w")
entrada_senha = tk.Entry(login_frame, show="*", width=30)
entrada_senha.pack(pady=5)

# Botões Registrar e Entrar
btn_frame = tk.Frame(login_frame)
btn_frame.pack(pady=10)
btn_registrar = tk.Button(btn_frame, text="Registrar", command=abrir_janela_cadastro)
btn_registrar.pack(side="left", padx=5)
btn_entrar = tk.Button(btn_frame, text="Entrar", command=entrar)
btn_entrar.pack(side="right", padx=5)

# Executar a interface
root.mainloop()
