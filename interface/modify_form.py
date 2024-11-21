import customtkinter as ctk
from app.user_data import verify_user, find_user_by_id, add_new_user, update_user_in_excel 
from app.training_data import get_training_data

# Define la lista de carreras (opciones disponibles para la selección)
opciones1 = [
    "Arquitectura", "Administración de empresas con Especialización en Transformación Digital",
    "Antropología", "Arqueología", "Baccalaureatus en Artibus", "Baccalaureatus en Scientiis",
    "Composición y Producción Musical", "Diseño de Producto e innovación", "International Marketing and Business Analytics",
    "Psicología", "Relaciones internacionales", "Biología", "Bioquímica y Microbiología", "Biotecnología Molecular",
    "Comunicación Estratégica", "Física", "Matemática Aplicada", "Nutrición", "Química", "Química Farmacéutica",
    "Ingeniería Biomédica", "Ingeniería en Biotecnología Industrial", "Ingeniería en Ciencia de los Alimentos",
    "Ingeniería en Ciencia de los alimentos Industrial", "Ingeniería en Ciencias de la Administración",
    "Ingeniería en Ciencia de los Datos", "Ingeniería Civil", "Ingeniería Civil Ambiental",
    "Ingeniería Civil Arquitectónica", "Ingeniería Civil Industrial", "Ingeniería en Ciencia de la computación y Tecnologías de la información",
    "Ingeniería Electrónica", "Ingeniería Industrial", "Ingeniería Mecánica", "Ingeniería Mecánica Industrial",
    "Ingeniería Mecatrónica", "Ingeniería Química", "Ingeniería Química Industrial",
    "Profesorado de Enseñanza Media Especializado en Educación Musical",
    "Profesorado de Enseñanza Media especializado en English Language Teaching (ELT)",
    "Profesorado Especializado en Educación Inclusiva", "Profesorado Especializado en Educación Primaria (100% virtual)",
    "Profesorado Especializado en Problemas del Aprendizaje", "Profesorado de Enseñanza Media Especializado en Matemática y Ciencias Físicas",
    "Profesorado de Enseñanza Media Especializado en Ciencias Químicas y Biológicas",
    "Profesorado de Enseñanza Media Especializado en Ciencias Sociales",
    "Profesorado de Enseñanza Media Especializado en Comunicación y Lenguaje", "Otra"
]

def modify_user_form(parent, colors):
    # Define input variables
    first_name_var = ctk.StringVar()
    second_name_var = ctk.StringVar()
    first_surname_var = ctk.StringVar()
    second_surname_var = ctk.StringVar()
    id_number_var = ctk.StringVar()
    career_name_var = ctk.StringVar()
    role_name_var = ctk.StringVar(value="Estudiante")  # Default value for ROL
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

    # Function to handle user modification logic
    def submit_user():
        carnet = id_number_var.get().strip()
        # Validate numeric ID
        if not carnet.isdigit():
            message_var.set("Error: El carnet debe ser un número")
            return
        
        carnet = int(carnet)

        user_data = find_user_by_id(carnet)
        
        if user_data is None:
            message_var.set("Usuario no encontrado.")
        else:
            # Modify the user data
            modified_user = {
                "Primer Nombre": first_name_var.get(),
                "Segundo Nombre": second_name_var.get(),
                "Primer apellido": first_surname_var.get(),
                "Segundo apellido": second_surname_var.get(),
                "Carnet": carnet,
                "Carrera": career_name_var.get(),
                "ROL": role_name_var.get(),
                # Save selected trainings as a list of IDs (numbers)
                "Capacitaciones": ', '.join(map(str, selected_trainings))  # Convert to string of numbers
            }

            # Attempt to update the user in the Excel file
            if update_user_in_excel(modified_user):
                message_var.set("Usuario modificado exitosamente")
                message_label.configure(text_color="green")
            else:
                message_var.set("Error al modificar usuario")
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

    # Career selectbox
    ctk.CTkLabel(parent, text="Carrera: ").grid(row=5, column=0, padx=10, pady=10)
    career_selectbox = ctk.CTkOptionMenu(parent, variable=career_name_var,
                                         values=opciones1, fg_color=colors["mauve"],
                                         button_hover_color=colors["maroon"],
                                         button_color=colors["peach"])
    career_selectbox.grid(row=5, column=1, padx=10, pady=10)
    
    # ROL selectbox
    ctk.CTkLabel(parent, text="ROL: ").grid(row=6, column=0, padx=10, pady=10)
    role_selectbox = ctk.CTkOptionMenu(parent, variable=role_name_var,
                                       values=["Estudiante", "Auxiliar"],
                                       fg_color=colors["mauve"], button_hover_color=colors["maroon"],
                                       button_color=colors["peach"])
    role_selectbox.grid(row=6, column=1, padx=10, pady=10)

    # Training selection label and checkboxes
    ctk.CTkLabel(parent, text="Capacitaciones: ").grid(row=7, column=0, padx=10, pady=10)

    # Create a checkbox for each available training
    row = 8  # Start from row 8 for checkbox placement
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
        row += 1

    # Toggle function for adding/removing training from the selected list
    def toggle_training(training):
        # Add or remove the training ID (number) from the selected list
        training_id = training_map[training]
        if training_id in selected_trainings:
            selected_trainings.remove(training_id)
        else:
            selected_trainings.append(training_id)

    # Add user button calling submit_user
    submit_button = ctk.CTkButton(
        parent,
        text="Modificar Usuario",
        command=submit_user,
        fg_color=colors["mauve"],
        hover_color=colors["maroon"],
        text_color=colors["crust"],
    )
    submit_button.grid(row=row, column=0, columnspan=2, padx=10, pady=10)

