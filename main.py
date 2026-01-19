import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    filename=file_Entry.get().strip()
    data = data_Entry.get().strip()

    if not filename or not data:
        messagebox.showerror("Input Error", "Both filename and data fields must be filled.")
        return
    qr_img=qrcode.make(data)
    qr_img.save(f"{filename}.png")

    img=qr_img.resize((180,180))
    img_tk=ImageTk.PhotoImage(img)

    qr_label.config(image=img_tk,text="")
    qr_label.image=img_tk
    messagebox.showinfo("Success",f"QR code saved as {filename}.png")

root=tk.Tk()
root.title("QR code Generator")
root.geometry("400x400")
root.config(bg="white")
title_label=tk.Label(root,text="QR code Generator",font=("Arial",16,"bold"),bg="White",fg="black")
title_label.pack(pady=20)

input_frame=tk.Frame(root,bg="white")
input_frame.pack(pady=10)
tk.Label(
    input_frame,text="filename:",font=("Helvetica",14),
    bg="white"
).grid(row=0,column=0,padx=10,pady=10,sticky="e")
file_Entry=tk.Entry(input_frame,font=("Helvetica",14),width=25)
file_Entry.grid(row=0,column=1)

tk.Label(
    input_frame,text="QR Data:",font=("Helvetica",14),
    bg="white"
).grid(row=1,column=0,padx=10,pady=10,sticky="e")
data_Entry=tk.Entry(input_frame,font=("Helvetica",14),width=25)
data_Entry.grid(row=1,column=1)
generate_btn=tk.Button(
    root,text="Generate QR code",font=("Helvetica",22),
    bg="green",
    fg="white",
    width=20,
    command=generate_qr
)
generate_btn.pack(pady=20)
qr_frame=tk.Frame(root,bg="white",width=200,height=200)

qr_frame.pack(pady=10)
qr_frame.pack_propagate(False)
qr_label=tk.Label(qr_frame,text="QR CODE WILL APPEAR  HERE",font=("helvetica",12),bg="white",fg="black")

qr_label.pack(expand=True)

root.mainloop()