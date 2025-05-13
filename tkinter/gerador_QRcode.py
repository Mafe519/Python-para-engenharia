import qrcode
from tkinter import Tk, Label, Entry, Button
from PIL import Image, ImageTk
from tkinter import filedialog

def criar_qr_code():
    texto = entry_texto.get() # <--- funbção para pegar o texto
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    global qr_image
    qr_image = qr.make_image(fill='black', back_color='white')
    qr_image.save("qrcode.png")  # Salva a imagem do QR Code
    show_qr_code(qr_image)


def show_qr_code(img): # <--- função para exibir o qr code no nosso aplicativo
    img = img.resize((150, 150))  
    photo = ImageTk.PhotoImage(img)
    qr_label.imgtk = photo
    qr_label.configure(image=photo)
    qr_label.image = photo

root = Tk()  # <--- função para criar a janela
root.title("Gerador de QR Code")
root.geometry("300x300")  

Label(root, text="Digite o texto para o QR Code:").pack()
entry_texto = Entry(root)
entry_texto.pack()

Button(root, text="Gerar QR Code", command=criar_qr_code).pack()


qr_label = Label(root) 
qr_label.pack()


def salvar_qr_code(): # <--- função para salvar o QR Code
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if filename:
        qr_image.save(filename)

Button(root, text="Salvar QR Code", command=salvar_qr_code).pack()


root.mainloop()

#