import customtkinter as ctk
from app.user_data import add_new_user, verify_user

# New user form interface
import customtkinter as ctk
from app.user_data import add_new_user, verify_user
from app.training_data import get_training_data

# New user form interface
def new_user_form(parent, colors):
    # Define input variables
    first_name_var = ctk.StringVar()
    second_name_var = ctk.StringVar()
    first_surname_var = ctk.StringVar()
    second_surname_var = ctk.StringVar()
    id_number_var = ctk.StringVar()
    career_name_var = ctk.StringVar()
    message_var = ctk.StringVar()

    # Load available trainings
    training_data = get_training_data()  # Load training data
    available_trainings = training_data['Capacitación'].tolist()

    # State message label
    message_label = ctk.CTkLabel(parent, textvariable=message_var)
    message_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Function to handle user registration logic
    def submit_user():
        first_name = first_name_var.get()
        carnet = id_number_var.get()
        
        # Validate numeric ID
        if not carnet.isdigit():
            message_var.set("Error: El carnet debe ser un número")
            return

        # Verify if user already exists
        if verify_user(first_name, carnet):
            message_var.set("Error, ya existe este usuario")
        else:
            new_user = {
                "Primer Nombre": first_name_var.get(),
                "Segundo Nombre": second_name_var.get(),
                "Primer apellido": first_surname_var.get(),
                "Segundo apellido": second_surname_var.get(),
                "Carnet": id_number_var.get(),
                "Carrera": career_name_var.get(),
                "Capacitaciones": ', '.join(training_selection_var.get())  # Save selected trainings as comma-separated string
            }

            # Attempt to add the new user
            if add_new_user(new_user):
                message_var.set("Usuario agregado")
                message_label.configure(text_color="green")
            else:
                message_var.set("Error al agregar usuario")
                message_label.configure(text_color="red")

    # Create labels and entry fields for the form
    ctk.CTkLabel(parent, text="Primer Nombre: ").grid(row=0, column=0, padx=10, pady=10)
    ctk.CTkEntry(parent, textvariable=first_name_var).grid(row=0, column=1, padx=10, pady=10)

    ctk.CTkLabel(parent, text="Segundo Nombre: ").grid(row=1, column=0, padx=10, pady=10)
    ctk.CTkEntry(parent, textvariable=second_name_var).grid(row=1, column=1, padx=10, pady=10)

    ctk.CTkLabel(parent, text="Primer Apellido: ").grid(row=2, column=0, padx=10, pady=10)
    ctk.CTkEntry(parent, textvariable=first_surname_var).grid(row=2, column=1, padx=10, pady=10)

    ctk.CTkLabel(parent, text="Segundo Apellido: ").grid(row=3, column=0, padx=10, pady=10)
    ctk.CTkEntry(parent, textvariable=second_surname_var).grid(row=3, column=1, padx=10, pady=10)

    ctk.CTkLabel(parent, text="Carnet: ").grid(row=4, column=0, padx=10, pady=10)
    ctk.CTkEntry(parent, textvariable=id_number_var).grid(row=4, column=1, padx=10, pady=10)

    ctk.CTkLabel(parent, text="Carrera: ").grid(row=5, column=0, padx=10, pady=10)
    ctk.CTkEntry(parent, textvariable=career_name_var).grid(row=5, column=1, padx=10, pady=10)

    # Training selection label and combo box
    ctk.CTkLabel(parent, text="Capacitaciones: ").grid(row=6, column=0, padx=10, pady=10)
    training_selection_var = ctk.StringVar(value=available_trainings)  # Default to all available trainings
    training_selection = ctk.CTkComboBox(
        parent,
        values=available_trainings,  # Options from the loaded training data
        variable=training_selection_var,
        state="readonly"  # Ensure it’s not editable
    )
    training_selection.grid(row=6, column=1, padx=10, pady=10)

    # Add user button calling submit_user
    submit_button = ctk.CTkButton(
        parent,
        text="Agregar Usuario",
        command=submit_user,
        fg_color=colors["mauve"],
        hover_color=colors["maroon"],
        text_color=colors["crust"],
    )
    submit_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

