import customtkinter as ctk
from interface.color_theme import get_palette
from app.user_data import find_user_by_id

def create_tabs(parent, colors):
    # Crear un Tabview para las tres pestañas
    tabview = ctk.CTkTabview(parent)
    tabview.grid(row=0, column=0, padx=20, pady=20)

    # Crear las tres pestañas
    tabview.add("Buscar Usuario")
    tabview.add("Registrar Usuario")
    tabview.add("Otra Función")

    # Pestaña 1 - Buscar Usuario
    def search_user_tab(tab):
        # Entrada para carnet
        carnet_var = ctk.StringVar()
        ctk.CTkLabel(tab, text="Carnet: ").grid(row=0, column=0, padx=10, pady=10)
        carnet_entry = ctk.CTkEntry(tab, textvariable=carnet_var)
        carnet_entry.grid(row=0, column=1, padx=10, pady=10)

        # Función de búsqueda de usuario
        def search_user():
            carnet = carnet_var.get()
            user_data = find_user_by_id(carnet)
            if not user_data.empty:
                # Mostrar datos del usuario
                user_info = f"Nombre: {user_data.iloc[0]['Primer Nombre']} {user_data.iloc[0]['Segundo Nombre']}\n"
                user_info += f"Apellidos: {user_data.iloc[0]['Primer Apellido']} {user_data.iloc[0]['Segundo Apellido']}\n"
                user_info += f"Carrera: {user_data.iloc[0]['Carrera']}"
                user_data_label.configure(text=user_info)
            else:
                user_data_label.configure(text="Usuario no encontrado.")

        # Botón de búsqueda
        search_button = ctk.CTkButton(tab, text="Buscar Usuario", command=search_user, 
                                      fg_color=colors["mauve"], hover_color=colors["maroon"], text_color=colors["crust"])
        search_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Label para mostrar los datos del usuario
        user_data_label = ctk.CTkLabel(tab, text="")
        user_data_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Pestaña 2 - Registrar Usuario
    def register_user_tab(tab):
        from interface.form import new_user_form
        new_user_form(tab, colors)  # Usamos la función ya definida para registrar un nuevo usuario

    # Pestaña 3 - Otra Función (Puedes agregar la funcionalidad que desees)
    def another_function_tab(tab):
        label = ctk.CTkLabel(tab, text="Otra funcionalidad aquí.")
        label.grid(row=0, column=0, padx=10, pady=10)

    # Asociar cada función a su respectiva pestaña
    search_user_tab(tabview.tab("Buscar Usuario"))
    register_user_tab(tabview.tab("Registrar Usuario"))
    another_function_tab(tabview.tab("Otra Función"))

# Crear la aplicación
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

    # Crear las pestañas
    create_tabs(app, colors)

    app.mainloop()

