import customtkinter as ctk

root = ctk.CTk()

# Configurando a janela principal
root.title("App teste")
root.geometry("700x400")
root.maxsize(width=900, height=550)
root.minsize(width=500, height=300)
root.resizable(width=True, height=True)

# Frames
frame1 = ctk.CTkFrame(root, width=200, height=330, fg_color="teal", bg_color="red", border_width=2).place(x=10, y=60)
frame2 = ctk.CTkFrame(master=root, width=200, height=330, fg_color="green").place(x=230, y=60)
frame3 = ctk.CTkFrame(root, width=200, height=330, fg_color="gray").place(x=450, y=60)
root.mainloop()