import customtkinter as ctk
from interface.color_theme import get_palette
from interface.tabs import create_tabs
from interface.layout import create_layout

# Update layout by tabview
def update_layout(parent, colors, tab):
    # Clean the existing frames
    for widget in parent.winfo_children():
        widget.destroy()

    if tab == "Registro Auxiliares":
        create_layout(parent, colors, "Registro Auxiliares")
    elif tab == "Datos Estudiantes":
        create_layout(parent, colors, "Datos Estudiantes")
    elif tab == "Registro Entrada Estudiantes":
        create_layout(parent, colors, "Registro Entrada Estudiantes")

# Main Interface
def create_app():
    # Interface init
    app = ctk.CTk()
    app.title("D-HIVE")
    app.attributes('-fullscreen', True)

    # Color theme init
    ctk.set_appearance_mode('light')
    colors = get_palette()

    # App configuration
    app.configure(fg_color=colors["base"])
    
    # Create tabs
    tabs = create_tabs(app, colors)
    tabs.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    update_layout(app, colors, tabs.get())

    return app
