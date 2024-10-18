import customtkinter as ctk
from app.user_data import add_new_user, verify_user, get_trainings

# Funcion para crear un formulario (frontend) para ingresar datos del nuevo usuario
def new_user_form(parent):
    first_name_var = ctk.StringVar()
    second_name_var = ctk.StringVar()
    first_surname_var = ctk.StringVar()
    second_surname_var = ctk.StringVar()
    id_number_var = ctk.StringVar()
    career_name_var = ctk.StringVar()
    message_var = ctk.StringVar()
    message_label = None

    # Crear tags y campos de entrada para el formulario de usuario nuevo

    ctk.CTkLabel(parent, text="Primer Nombre: ").grid(row=0, column=0, padx=10, pady=10,)
    ctk.CTkEntry(parent, textvariable=first_name_var).grid(row=0, column=1, padx=10, pady=10)
    
    ctk.CTkLabel(parent, text="Segundo Nombre: ").grid(row=1, column=0, padx=10, pady=10,)
    ctk.CTkEntry(parent, textvariable=second_name_var).grid(row=1, column=1, padx=10, pady=10)
    
    ctk.CTkLabel(parent, text="Primer Apellido: ").grid(row=2, column=0, padx=10, pady=10,)
    ctk.CTkEntry(parent, textvariable=first_surname_var).grid(row=2, column=1, padx=10, pady=10)
    
    ctk.CTkLabel(parent, text="Segundo Apellido: ").grid(row=3, column=0, padx=10, pady=10,)
    ctk.CTkEntry(parent, textvariable=second_surname_var).grid(row=3, column=1, padx=10, pady=10)
    
    ctk.CTkLabel(parent, text="Carnet: ").grid(row=4, column=0, padx=10, pady=10,)
    ctk.CTkEntry(parent, textvariable=id_number_var).grid(row=4, column=1, padx=10, pady=10)
    
    ctk.CTkLabel(parent, text="Carrera: ").grid(row=5, column=0, padx=10, pady=10,)
    ctk.CTkEntry(parent, textvariable=career_name_var).grid(row=5, column=1, padx=10, pady=10)

    # Boton para enviar el formulario
    submit_button = ctk.CTkButton(parent, text="Agregar Usuario", command=submit_user)
    submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Funcion para ingresar los datos y verificar que sean validos
def submit_user():
    first_name = first_name_var.get()
    carnet = id_number_var.get()

    if not carnet.isdigit():
        message_var.set("Error: El carnet debe ser un número")
        return

    if verify_user(first_name, carnet):
        message_var.set("Error, ya existe este usuario")
    else:
        new_user = {
                "Primer Nombre": first_name_var.get(),
                "Segundo Nombre": second_name_var.get(),
                "Primer Apellido": first_surname_var.get(),
                "Segundo Apellido": second_name_var.get(),
                "Carnet": id_number_var.get(),
                "Carrera": career_name_var.get()
        }

        if add_new_user(new_user):
            message_var.set("Usuario agregado")
            message_label.configure(text_color="green")
        else:
            message_var.set("Erro al agregar usuario")
            message_label.configure(text_color="red")

