import customtkinter as ctk
from app.user_data import get_users_data, update_user_data
from app.training_data import get_training_data

def modify_user_form(parent, colors):
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

    # Map each training to a number (ID)
    training_map = {training: index + 1 for index, training in enumerate(available_trainings)}

    # Store selected training IDs
    selected_trainings = []

    # State message label
    message_label = ctk.CTkLabel(parent, textvariable=message_var)
    message_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Function to load user data into fields
    # Function to load user data into fields
    def load_user_data(carnet):
        # Verify that carnet is a valid integer
        try:
            carnet = int(carnet.strip())
        except ValueError:
            message_var.set("Formato de carnet inválido.")
            return
        # Search the user by carnet
        user_data = get_users_data()
        user = user_data[user_data['Carnet'] == carnet]	
        if not user.empty:
            # Fill fields with current user data
            first_name_var.set(user.iloc[0]["Primer Nombre"])
            second_name_var.set(user.iloc[0]["Segundo Nombre"])
            first_surname_var.set(user.iloc[0]["Primer apellido"])
            second_surname_var.set(user.iloc[0]["Segundo apellido"])
            career_name_var.set(user.iloc[0]["Carrera"])
            # Load trainings
            current_trainings = user.iloc[0]["Capacitaciones"].split(', ')
            selected_trainings[:] = [int(t) for t in current_trainings if t.isdigit()]
            # Update checkbox state based on current trainings
            for training in available_trainings:
                training_id = training_map.get(training)
                if training_id in selected_trainings:
                    checkbox = training_checkboxes[training]
                    checkbox.select()
            message_var.set(f"Datos cargados para el carnet: {carnet}")
        else:
            message_var.set("No se encontró el usuario con ese carnet")

    # Function to handle user modification
    def modify_user():
        carnet = id_number_var.get()
        
        # Verify user existence
        user_data = get_users_data()
        user = user_data[user_data['Carnet'] == carnet]
        
        if user.empty:
            message_var.set("No se encontró el usuario con ese carnet")
            return

        updated_data = {
            "Primer Nombre": first_name_var.get(),
            "Segundo Nombre": second_name_var.get(),
            "Primer apellido": first_surname_var.get(),
            "Segundo apellido": second_surname_var.get(),
            "Carrera": career_name_var.get(),
            "Capacitaciones": ', '.join(map(str, selected_trainings))  # Convert to string of numbers
        }

        if update_user_data(carnet, updated_data):
            message_var.set("Datos actualizados con éxito")
            message_label.configure(text_color="green")
        else:
            message_var.set("Error al actualizar los datos")
            message_label.configure(text_color="red")

    # Create labels and entry fields for the form
    ctk.CTkLabel(parent, text="Carnet (para buscar y modificar): ").grid(row=0, column=0, padx=10, pady=10)
    ctk.CTkEntry(parent, textvariable=id_number_var).grid(row=0, column=1, padx=10, pady=10)

    ctk.CTkLabel(parent, text="Primer Nombre: ").grid(row=1, column=0, padx=10, pady=10)
    ctk.CTkEntry(parent, textvariable=first_name_var).grid(row=1, column=1, padx=10, pady=10)

    ctk.CTkLabel(parent, text="Segundo Nombre: ").grid(row=2, column=0, padx=10, pady=10)
    ctk.CTkEntry(parent, textvariable=second_name_var).grid(row=2, column=1, padx=10, pady=10)

    ctk.CTkLabel(parent, text="Primer Apellido: ").grid(row=3, column=0, padx=10, pady=10)
    ctk.CTkEntry(parent, textvariable=first_surname_var).grid(row=3, column=1, padx=10, pady=10)

    ctk.CTkLabel(parent, text="Segundo Apellido: ").grid(row=4, column=0, padx=10, pady=10)
    ctk.CTkEntry(parent, textvariable=second_surname_var).grid(row=4, column=1, padx=10, pady=10)

    ctk.CTkLabel(parent, text="Carrera: ").grid(row=5, column=0, padx=10, pady=10)
    ctk.CTkEntry(parent, textvariable=career_name_var).grid(row=5, column=1, padx=10, pady=10)

    # Training selection label and checkboxes
    ctk.CTkLabel(parent, text="Capacitaciones: ").grid(row=6, column=0, padx=10, pady=10)

    training_checkboxes = {}

    # Create a checkbox for each available training
    row = 7  # Start from row 7 for checkbox placement
    for training in available_trainings:
        checkbox = ctk.CTkCheckBox(
            parent,
            text=training,
            command=lambda training=training: toggle_training(training),
            fg_color=colors["mauve"],
            hover_color=colors["maroon"],
            text_color=colors["text"]
        )
        checkbox.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        training_checkboxes[training] = checkbox
        row += 1

    # Toggle function for adding/removing training from the selected list
    def toggle_training(training):
        # Add or remove the training ID (number) from the selected list
        training_id = training_map[training]
        if training_id in selected_trainings:
            selected_trainings.remove(training_id)
        else:
            selected_trainings.append(training_id)

    # Modify user button calling modify_user
    modify_button = ctk.CTkButton(
        parent,
        text="Modificar Usuario",
        command=modify_user,
        fg_color=colors["mauve"],
        hover_color=colors["maroon"],
        text_color=colors["crust"],
    )
    modify_button.grid(row=row, column=0, columnspan=2, padx=10, pady=10)

    # Search user by carnet when ID is entered
    search_button = ctk.CTkButton(
        parent,
        text="Buscar Usuario",
        command=lambda: load_user_data(id_number_var.get()),
        fg_color=colors["mauve"],
        hover_color=colors["maroon"],
        text_color=colors["crust"],
    )
    search_button.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=10)

