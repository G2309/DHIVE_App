import customtkinter as ctk
from app.user_data import find_user_by_id, get_trainings
from interface.form import new_user_form
from interface.modify_form import modify_user_form

def setup_student_tab(tab, colors):
    """
    Sets up the layout and functionality for the 'Estudiantes' tab.
    """

    # Create left and right frames
    # Left frame = user options
    # Right frame = input
    left_frame = ctk.CTkFrame(tab, width=500, fg_color=colors["base"])
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

    right_frame = ctk.CTkFrame(tab, fg_color=colors["mantle"])
    right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    
    # Configure layout expansion
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(1, weight=1)

    # Function to show search interface
    def show_search_user():
        for widget in right_frame.winfo_children():
            widget.destroy()  # Clear right frame
        
        # Input for ID number
        carnet_var = ctk.StringVar()
        ctk.CTkLabel(right_frame, text="Carnet: ").grid(row=0, column=0, padx=10, pady=10)
        carnet_entry = ctk.CTkEntry(right_frame, textvariable=carnet_var)
        carnet_entry.grid(row=0, column=1, padx=10, pady=10)

        def search_user():
            try:
                carnet = int(carnet_var.get().strip())
            except ValueError:
                user_data_label.configure(text="Invalid carnet format.")
                return
            # Retrieve user data by ID
            user_data = find_user_by_id(carnet)
            if not user_data.empty:
                trainings = get_trainings(user_data.iloc[0]['Capacitaciones'])
                # New line for each training
                formatted_trainings = "\n".join(trainings)
                # Format of user info
                user_info = (
                    f"Rol: {user_data.iloc[0]['ROL']}\n"
                    f"Nombre: {user_data.iloc[0]['Primer Nombre']} {user_data.iloc[0]['Segundo Nombre']}\n"
                    f"Apellido: {user_data.iloc[0]['Primer apellido']} {user_data.iloc[0]['Segundo apellido']}\n"
                    f"Carrera: {user_data.iloc[0]['Carrera']}\n"
                    f"Bloqueos: {user_data.iloc[0]['Bloqueos']}\n"
                    f"Capacitaciones:\n{trainings}"
                )
                user_data_label.configure(text=user_info)
            else:
                user_data_label.configure(text="User not found.")

        # Search button
        search_button = ctk.CTkButton(right_frame, text="Buscar Usuario",
                                      command=search_user,
                                      fg_color=colors["mauve"],
                                      hover_color=colors["maroon"],
                                      text_color=colors["crust"])
        search_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Label to display user data
        user_data_label = ctk.CTkLabel(right_frame, text="")
        user_data_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Function to show register form
    def show_register_form():
        for widget in right_frame.winfo_children():
            widget.destroy()  # Clear right frame
        
        # Load the form
        new_user_form(right_frame, colors)

    # Function to show modify form
    def show_modify_form():
        for widget in right_frame.winfo_children():
            widget.destroy()  # Clear right frame
        
        # Load the modify user form
        modify_user_form(right_frame, colors)

    # Buttons in left frame for options
    search_button = ctk.CTkButton(left_frame, text="Buscar por ID",
                                  command=show_search_user, 
                                  fg_color=colors["mauve"],
                                  hover_color=colors["maroon"],
                                  text_color=colors["crust"])
    search_button.grid(row=0, column=0, padx=10, pady=10)

    register_button = ctk.CTkButton(left_frame, text="Registrar Usuario",
                                    command=show_register_form,
                                    fg_color=colors["mauve"],
                                    hover_color=colors["maroon"],
                                    text_color=colors["crust"])
    register_button.grid(row=1, column=0, padx=10, pady=10)

    modify_button = ctk.CTkButton(left_frame, text="Modificar Usuario",
                                  command=show_modify_form,
                                  fg_color=colors["mauve"],
                                  hover_color=colors["maroon"],
                                  text_color=colors["crust"])
    modify_button.grid(row=2, column=0, padx=10, pady=10)

