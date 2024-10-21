import customtkinter as ctk
from interface.form import new_user_form

# Function to organize frames and load content dynamically based on a selected tab
def create_layout(parent, colors, tab_name):
    if tab_name == "Registro Auxiliares":
        left_frame = ctk.CTkFrame(
                parent,
                width=500,
                height=700,
                fg_color=colors["base"]
                )
        left_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        
        ctk.CTkLabel(left_frame, text="Registro auxiliares"). grid(row=0, column=0)


    elif tab_name == "Registro Estudiantes":
        left_frame = ctk.CTkFrame(
                parent,
                width=500,
                height=700,
                fg_color=colors["base"]
                )
        left_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        
        new_user_form(left_frame, colors)
    
    elif tab_name == "Registro Entrada Estudiantes":
        left_frame = ctk.CTkFrame(
                parent,
                width=500,
                height=700,
                fg_color=colors["base"]
                )
        left_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        
        ctk.CTkLabel(left_frame, text="Registro Entrada Estudiantes"). grid(row=0, column=0)

    right_frame = ctk.CTkFrame(
            parent,
            width=500,
            height=700,
            fg_color=colors["base"]
            )
    right_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

    # Auto adjust the app if the windows is resized
    parent.grid_columnconfigure(0, weight=1)
    parent.grid_columnconfigure(1, weight=1)
    parent.grid_rowconfigure(0, weight=0)   # Tab row: No change if resize
    parent.grid_rowconfigure(1, weight=1)   # App row: Change if resize
