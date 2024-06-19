import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# mudar a imagem a cada erro
def update_image():
    global errors
    if errors < len(images):
        img_tk = images[errors]
        image_label.config(image=img_tk)
        image_label.image = img_tk

# mostrar algumas letras se acertar
def guess_letter():
    global errors
    letter = entry.get().lower()
    entry.delete(0, tk.END)

   # se a letra esta na palavra, mostra ela na palavra com todas as letras
    if letter in word:
        for idx, char in enumerate(word):
            if char == letter:
                word_display[idx] = letter
        word_label.config(text=" ".join(word_display))
    else:
        errors += 1        
        update_image()

    if errors == len(images):
        # mostra se o jogador perdeu
        messagebox.showinfo("Forca", "Você perdeu!")
    # mostra se o jogador venceu
    elif "_" not in word_display:
        messagebox.showinfo("Forca", "Você ganhou!")

errors = 0
word = "coke"
word_display = ["_" for _ in word]

root = tk.Tk()
root.title("Jogo da Forca")

# diretorio das imagens
image_paths = [
    "jogodaforca.png",
    "jogodaforca2.png",
    "jogodaforca3.png",
    "jogodaforca4.png",
    "jogodaforca5.png",
    "jogodaforca6.png",
    "jogodaforca7.png"
]
# mostra mensagem de erro se houver problema ao carregar as imagens
images = [ImageTk.PhotoImage(Image.open(path)) for path in image_paths]

img_tk = images[0]
image_label = tk.Label(root, image=img_tk)
image_label.pack()

word_label = tk.Label(root, text=" ".join(word_display), font=("Helvetica", 24))
word_label.pack()
# entrada para as letras
entry = tk.Entry(root)
entry.pack()

# botão para confirmar letra
guess_button = tk.Button(root, text="Adivinhar", command=guess_letter)
guess_button.pack()

root.mainloop()
