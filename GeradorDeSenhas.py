import random
import string
import tkinter as tk
from tkinter import messagebox

def gerar_senha():
   
    comprimento = int(entry_length.get())  
    caracteres = string.ascii_letters + string.digits + string.punctuation  
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))  

    entry_password.delete(0, tk.END)  
    entry_password.insert(0, senha)  

def copiar_senha():
    senha = entry_password.get()
    if senha:
        janela.clipboard_clear()  
        janela.clipboard_append(senha)  
        messagebox.showinfo("Senha copiada!", "A senha foi copiada para o clipboard.")
    else:
        messagebox.showwarning("Nada a copiar", "Gere uma senha primeiro.")


janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("400x200")


label_length = tk.Label(janela, text="Comprimento da senha:")
label_length.pack(pady=5)


entry_length = tk.Entry(janela)
entry_length.insert(0, "16")  
entry_length.pack(pady=5)


btn_generate = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
btn_generate.pack(pady=10)


entry_password = tk.Entry(janela, width=40)
entry_password.pack(pady=5)


btn_copy = tk.Button(janela, text="Copiar Senha", command=copiar_senha)
btn_copy.pack(pady=10)


janela.mainloop()
