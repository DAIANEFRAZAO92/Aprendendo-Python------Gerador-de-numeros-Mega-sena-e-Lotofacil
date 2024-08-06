import tkinter as tk
from tkinter import messagebox
import random 


def gerar_numeros_de_mega_sena():# esse é a função
    numeros =random.sample(range(1,61),6)
    numeros.sort()# sort é uam função que ordena os números em ordem crescente
    resultado_mega.config(text=f"Gerar números da Mega Sena: {numeros}") #esse vai gerar os números e exibir

def gerar_lotofacil():
    numeros =random.sample(range(1,26),15)
    numeros.sort()
    resultado_loto.config(text=f"Gerar números da lotofácil: {numeros}") #esse vai gerar os números



# Configurando a janela principal
root = tk.Tk()  # Cria a janela principal do aplicativo
# Define o título da janela principal
root.title("Gerador de Números Aleatórios")

# Configurando o layout
# Cria um frame dentro da janela principal com padding de 10 pixels
frame = tk.Frame(root, padx=10, pady=10)
# Empacota o frame na janela principal com padding de 10 pixels
frame.pack(padx=10, pady=10)

# Botão para Mega-Sena
# Cria um botão no frame para gerar números da Mega-Sena
btn_mega_sena = tk.Button(
    frame, text="Gerar Números da Mega-Sena", command=gerar_numeros_de_mega_sena)
# Posiciona o botão na primeira linha e coluna do grid e adiciona um padding vertical de 5 pixels
btn_mega_sena.grid(row=0, column=0, pady=5)

# Label para exibir resultado da Mega-Sena
# Cria um label no frame para exibir os números da Mega-Sena
resultado_mega = tk.Label(frame, text="Números da Mega-Sena: ")
# Posiciona o label na segunda linha e primeira coluna do grid e adiciona um padding vertical de 5 pixels
resultado_mega.grid(row=1, column=0, pady=5)

# Botão para Lotofácil
# Cria um botão no frame para gerar números da Lotofácil
btn_lotofacil = tk.Button(
    frame, text="Gerar Números da Lotofácil", command=gerar_lotofacil)
# Posiciona o botão na terceira linha e primeira coluna do grid e adiciona um padding vertical de 5 pixels
btn_lotofacil.grid(row=2, column=0, pady=5)

# Label para exibir resultado da Lotofácil
# Cria um label no frame para exibir os números da Lotofácil
resultado_loto = tk.Label(frame, text="Números da Lotofácil: ")
# Posiciona o label na quarta linha e primeira coluna do grid e adiciona um padding vertical de 5 pixels
resultado_loto.grid(row=3, column=0, pady=5)

# Iniciando o loop principal da interface gráfica
root.mainloop()