import customtkinter as ctk
from interface.color_theme import get_palette
from interface.student_tab import setup_student_tab  # Import the student tab setup function

def create_tabs(parent, colors):
    # Create the TabView for the 3 tabs
    tabview = ctk.CTkTabview(parent)
    tabview.grid(row=0, column=0, padx=20, pady=20)

    # Create the 3 tabs
    tabview.add("Estudiantes")
    tabview.add("Auxiliares")
    tabview.add("Algo")

    # Associate each function to its corresponding tab
    setup_student_tab(tabview.tab("Estudiantes"), colors)  # Load student tab layout
    
    # Tab2 - Assistants
    def assistants_tab(tab):
        left_frame = ctk.CTkFrame(tab, width=500, fg_color=colors["base"])
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

        right_frame = ctk.CTkFrame(tab, fg_color=colors["mantle"])
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        # Example content for assistants tab
        ctk.CTkLabel(right_frame, text="Contenido para la pestaña Auxiliares").grid(row=0, column=0)

    # Tab3 - Other Function
    def another_function_tab(tab):
        left_frame = ctk.CTkFrame(tab, width=500, fg_color=colors["base"])
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

        right_frame = ctk.CTkFrame(tab, fg_color=colors["mantle"])
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        label = ctk.CTkLabel(right_frame, text="Tab para algo que no se me ha ocurrido")
        label.grid(row=0, column=0, padx=10, pady=10)

    # Link each tab to its content setup
    assistants_tab(tabview.tab("Auxiliares"))
    another_function_tab(tabview.tab("Algo"))

# Create the application
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

