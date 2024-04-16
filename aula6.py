import customtkinter as ctk

root = ctk.CTk()

# Configurando a janela principal
root.title("App teste")
root.geometry("700x400")
root.maxsize(width=900, height=550)
root.minsize(width=500, height=300)
root.resizable(width=True, height=True)

# Tab view
tabview = ctk.CTkTabview(root, width=400, corner_radius=20, segmented_button_fg_color="red", segmented_button_selected_color="blue", segmented_button_selected_hover_color="yellow", segmented_button_unselected_color="green", segmented_button_unselected_hover_color="teal")
tabview.pack()
tabview.add("Nomes")
tabview.add("Idades")
tabview.add("Sexo")
tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(0, weight=1)
tabview.tab("Sexo").grid_columnconfigure(0, weight=1)

# Adicionando elementos na tab
text = ctk.CTkLabel(tabview.tab("Nomes"), text="Kauã Lúcio\n Kevin Abraão \n Kaio Lúcio\n Maria Luzia")
text.pack()

idade = ctk.CTkLabel(tabview.tab("Idades"), text="20\n 27 \n 14\n 21")
idade.pack()

sexo = ctk.CTkLabel(tabview.tab("Sexo"), text="Masculino\n Masculino \n Masculino\n Feminino")
sexo.pack()

root.mainloop()