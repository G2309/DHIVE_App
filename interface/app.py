import customtkinter as ctk
from interface.color_theme import get_palette
from app.user_data import find_user_by_id
def create_tabs(parent, colors):
    # Create the TabView for the 3 tabs
    tabview = ctk.CTkTabview(parent)
    tabview.grid(row=0, column=0, padx=20, pady=20)

    # Create the 3 tabs
    tabview.add("Estudiantes")
    tabview.add("Auxiliares")
    tabview.add("Algo")

    # Tab1 - Students
    def search_user_tab(tab):
        # Entrada para carnet
        carnet_var = ctk.StringVar()
        ctk.CTkLabel(tab, text="Carnet: ").grid(row=0, column=0, padx=10, pady=10)
        carnet_entry = ctk.CTkEntry(tab, textvariable=carnet_var)
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
                # Format of user info
                user_info = (
                    f"Name: {user_data.iloc[0]['Primer Nombre']} {user_data.iloc[0]['Segundo Nombre']}\n"
                    f"Last Name: {user_data.iloc[0]['Primer apellido']} {user_data.iloc[0]['Segundo apellido']}\n"
                    f"Career: {user_data.iloc[0]['Carrera']}"
                )
                user_data_label.configure(text=user_info)
            else:
                user_data_label.configure(text="User not found.")


        # Search button
        search_button = ctk.CTkButton(tab, text="Buscar Usuario",
                                      command=search_user,
                                      fg_color=colors["mauve"],
                                      hover_color=colors["maroon"],
                                      text_color=colors["crust"])
        search_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Label to display user data
        user_data_label = ctk.CTkLabel(tab, text="")
        user_data_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Tab2 - Assistants
    def register_user_tab(tab):
        from interface.form import new_user_form
        new_user_form(tab, colors)  # Usamos la función ya definida para registrar un nuevo usuario

    # Tab3 - Do not know ?¿
    def another_function_tab(tab):
        label = ctk.CTkLabel(tab, text="Tab para algo que no se me ha ocurrido")
        label.grid(row=0, column=0, padx=10, pady=10)

    # Link each function to its corresponding tab
    search_user_tab(tabview.tab("Estudiantes"))
    register_user_tab(tabview.tab("Auxiliares"))
    another_function_tab(tabview.tab("Algo"))

# Create tab
def create_app():
    global left_frame, right_frame, colors

    # Interface init
    app = ctk.CTk()
    app.title("D-HIVE")
    app.attributes('-fullscreen', True)

    # Color theme init
    ctk.set_appearance_mode('light')
    colors = get_palette()

    app.configure(fg_color=colors["base"])

    # Create tabs
    create_tabs(app, colors)

    app.mainloop()

    return app

