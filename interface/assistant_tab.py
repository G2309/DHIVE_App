import customtkinter as ctk
from app.assistant_data import register_entry, get_last_record_number  # Importa la función para registrar asistencia

def setup_assistant_tab(tab, colors):
    """
    Sets up layout and functionality for the 'Auxiliares' tab.
    """
    # Create left and right frames
    left_frame = ctk.CTkFrame(tab, width=500, fg_color=colors["base"])
    left_frame.grid(row=0, column=0, padx=10, pady=20, sticky="ns")

    right_frame = ctk.CTkFrame(tab, fg_color=colors["mantle"])
    right_frame.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")
    
    # Button to show the 'Register Attendance' form
    register_button = ctk.CTkButton(
        left_frame, 
        text="Registrar Asistencia", 
        command=lambda: show_register_form(right_frame, colors),
        fg_color=colors["mauve"],
        hover_color=colors["maroon"]
    )
    register_button.grid(row=0, column=0, padx=10, pady=10)

def show_register_form(frame, colors):
    """
    Displays the attendance registration form in the right frame.
    """
    # Clear previous content in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Form title
    title_label = ctk.CTkLabel(frame, text="Registro de Asistencia", font=("Arial", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Form fields
    entry_labels = ["Primer nombre", "Segundo nombre", "Primer apellido", "Segundo apellido", "Carnet"]
    entries = {}

    for i, label_text in enumerate(entry_labels):
        label = ctk.CTkLabel(frame, text=label_text)
        label.grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
        
        entry = ctk.CTkEntry(frame)
        entry.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")
        entries[label_text] = entry

    # Time selection
    time_slots = {
        "07:00 - 10:00": ("07:00", "10:00"),
        "10:00 - 13:00": ("10:00", "13:00"),
        "13:00 - 16:00": ("13:00", "16:00"),
        "16:00 - 19:00": ("16:00", "19:00")
    }

    time_label = ctk.CTkLabel(frame, text="Turno de Asistencia")
    time_label.grid(row=len(entry_labels) + 1, column=0, padx=10, pady=5, sticky="e")
    
    time_var = ctk.StringVar(value="07:00 - 10:00")
    time_dropdown = ctk.CTkOptionMenu(frame, variable=time_var, values=list(time_slots.keys()))
    time_dropdown.grid(row=len(entry_labels) + 1, column=1, padx=10, pady=5, sticky="w")

    # Submit button
    submit_button = ctk.CTkButton(
        frame, 
        text="Guardar Asistencia", 
        command=lambda: save_entry(entries, time_var, time_slots, frame, colors),
        fg_color=colors["mauve"],
        hover_color=colors["maroon"]
    )
    submit_button.grid(row=len(entry_labels) + 2, column=0, columnspan=2, pady=20)

def save_entry(entries, time_var, time_slots, frame, colors):
    """
    Saves the attendance entry to the Excel file.
    """
    # Retrieve values from entries
    data = {label: entry.get() for label, entry in entries.items()}
    
    # Add time information
    data["Hora entrada"], data["Hora salida"] = time_slots[time_var.get()]

    # Get the current max "No.Registro" and increment by 1
    # Assuming `get_last_record_number` is a function that retrieves the last record number from the file/database
    last_record = get_last_record_number()
    data["No.Registro"] = last_record + 1

    # Call the backend function to register the entry
    register_entry(data)

    # Display success message in the GUI
    success_message = ctk.CTkLabel(frame, text="Asistencia registrada con éxito", fg_color=colors["green"], font=("Arial", 12, "bold"))
    success_message.grid(row=len(entries) + 3, column=0, columnspan=2, pady=10)

    # Automatically clear the message after a short delay
    frame.after(3000, success_message.destroy)  # Clears message after 3 seconds

