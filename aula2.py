import customtkinter as ctk

root = ctk.CTk()

# Configurando a janela principal
root.title("App teste")
root.geometry("700x400")
root.maxsize(width=900, height=550)
root.minsize(width=500, height=300)
root.resizable(width=True, height=True)
# root.iconify()
# root.deiconify()

root.mainloop()