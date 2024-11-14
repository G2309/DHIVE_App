import customtkinter as ctk
from interface.color_theme import get_palette
from interface.student_tab import setup_student_tab  # Import the student tab setup function
from interface.assistant_tab import setup_assistant_tab  # Import the assistant tab setup function

def create_tabs(parent, colors):
    # Create the TabView for the 3 tabs
    tabview = ctk.CTkTabview(parent)
    tabview.grid(row=0, column=0, padx=20, pady=20)
    tabview.configure(require_redraw=True, fg_color=colors["mantle"])

    # Create the 3 tabs
    tabview.add("Estudiantes")
    tabview.add("Auxiliares")

    # Associate each function to its corresponding tab
    setup_student_tab(tabview.tab("Estudiantes"), colors)  # Load student tab layout
    setup_assistant_tab(tabview.tab("Auxiliares"), colors)  # Load assistant tab layout
    

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

