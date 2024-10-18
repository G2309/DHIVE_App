import customtkinter as ctk

# Function to create tabs
def create_tabs(parent, colors):
    tabview = ctk.CTkTabview(
            parent,
            width=800,
            height=100,
            corner_radius=30,
            fg_color=colors["surface0"]
            )

    tabview.add("Registro Auxiliares")
    tabview.add("Datos Estudiantes")
    tabview.add("Registro Entrada Estudiantes")

    # Tabs configuration
    label_tab1 = ctk.CTkLabel(
            tabview.tab("Registro Auxiliares"),
            text="Registro Auxiliares",
            corner_radius=30,
            fg_color=colors["surface0"]
            )
    label_tab1.pack(padx=10, pady=10)

    label_tab1 = ctk.CTkLabel(
            tabview.tab("Datos Estudiantes"),
            text="Datos Estudiantes",
            corner_radius=30,
            fg_color=colors["surface0"]
            )
    label_tab1.pack(padx=10, pady=10)

    label_tab1 = ctk.CTkLabel(
            tabview.tab("Registro Entrada Estudiantes"),
            text="Registro Entrada Estudiantes",
            corner_radius=30,
            fg_color=colors["surface0"]
            )
    label_tab1.pack(padx=10, pady=10)

    return tabview
