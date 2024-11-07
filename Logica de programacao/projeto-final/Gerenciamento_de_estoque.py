import tkinter as tk
from tkinter import messagebox

# Função para exibir o formulário de entrada
def mostrar_formulario():
    form_frame.pack(side=tk.TOP, fill=tk.X)

# Função para adicionar o veículo (simples exemplo de mensagem)
def adicionar_veiculo():
    placa = placa_entrada.get()
    ano = ano_entrada.get()
    marca = marca_entrada.get()
    modelo = modelo_entrada.get()
    cor = cor_entrada.get()
    categoria = categoria_entrada.get()
    preco = preco_entrada.get()
    estado = estado_entrada.get()

    if placa and ano and marca and modelo and cor and categoria and preco and estado:
        # Aqui chamaria a função que realmente adiciona ao banco, por enquanto, mostra mensagem de confirmação
        messagebox.showinfo("Sucesso", "Veículo adicionado com sucesso!")
        # Limpar os campos após adicionar
        placa_entrada.delete(0, tk.END)
        ano_entrada.delete(0, tk.END)
        marca_entrada.delete(0, tk.END)
        modelo_entrada.delete(0, tk.END)
        cor_entrada.delete(0, tk.END)
        categoria_entrada.delete(0, tk.END)
        preco_entrada.delete(0, tk.END)
        estado_entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

# Janela principal
root = tk.Tk()
root.title("Gerenciador de Veículos")
root.geometry("400x400")

# Botão para exibir o formulário
btn_mostrar_formulario = tk.Button(root, text="Adicionar Veículo", command=mostrar_formulario)
btn_mostrar_formulario.pack(pady=10)

# Frame do formulário, inicialmente oculto
form_frame = tk.Frame(root, padx=10, pady=10)

# Campos do formulário (inicialmente ocultos)
tk.Label(form_frame, text="Placa:").grid(row=0, column=0, padx=5, pady=5)
placa_entrada = tk.Entry(form_frame)
placa_entrada.grid(row=1, column=0, padx=5, pady=5)

tk.Label(form_frame, text="Ano:").grid(row=2, column=0, padx=5, pady=5)
ano_entrada = tk.Entry(form_frame)
ano_entrada.grid(row=3, column=0, padx=5, pady=5)

tk.Label(form_frame, text="Marca:").grid(row=0, column=1, padx=5, pady=5)
marca_entrada = tk.Entry(form_frame)
marca_entrada.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Modelo:").grid(row=2, column=1, padx=5, pady=5)
modelo_entrada = tk.Entry(form_frame)
modelo_entrada.grid(row=3, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Cor:").grid(row=4, column=0, padx=5, pady=5)
cor_entrada = tk.Entry(form_frame)
cor_entrada.grid(row=5, column=0, padx=5, pady=5)

tk.Label(form_frame, text="Categoria:").grid(row=4, column=1, padx=5, pady=5)
categoria_entrada = tk.Entry(form_frame)
categoria_entrada.grid(row=5, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Preço:").grid(row=6, column=0, padx=5, pady=5)
preco_entrada = tk.Entry(form_frame)
preco_entrada.grid(row=7, column=0, padx=5, pady=5)

tk.Label(form_frame, text="Estado:").grid(row=6, column=1, padx=5, pady=5)
estado_entrada = tk.Entry(form_frame)
estado_entrada.grid(row=7, column=1, padx=5, pady=5)

# Botão de Adicionar dentro do formulário
btn_adicionar = tk.Button(form_frame, text="Adicionar", command=adicionar_veiculo)
btn_adicionar.grid(row=8, column=0, columnspan=2, pady=10)

# Executa a janela
root.mainloop()
