import customtkinter as ctk
from app.assistant_data import register_entry, get_last_record_number  # Importa la función para registrar asistencia
from datetime import datetime

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

    # Manual time entry
    entry_labels_time = ["Hora Entrada", "Hora Salida"]
    time_entries = {}

    for i, label_text in enumerate(entry_labels_time):
        label = ctk.CTkLabel(frame, text=label_text)
        label.grid(row=len(entry_labels) + i + 1, column=0, padx=10, pady=5, sticky="e")
        
        entry = ctk.CTkEntry(frame)
        entry.grid(row=len(entry_labels) + i + 1, column=1, padx=10, pady=5, sticky="w")
        time_entries[label_text] = entry

    # Submit button
    submit_button = ctk.CTkButton(
        frame, 
        text="Guardar Asistencia", 
        command=lambda: save_entry(entries, time_entries, frame, colors),
        fg_color=colors["mauve"],
        hover_color=colors["maroon"]
    )
    submit_button.grid(row=len(entry_labels) + len(entry_labels_time) + 2, column=0, columnspan=2, pady=20)

def save_entry(entries, time_entries, frame, colors):
    """
    Saves the attendance entry to the Excel file.
    """
    # Retrieve values from entries
    data = {label: entry.get() for label, entry in entries.items()}
    
    # Add manual time information
    data["Hora entrada"] = time_entries["Hora Entrada"].get()
    data["Hora salida"] = time_entries["Hora Salida"].get()

    # Get the current max "No.Registro" and increment by 1
    last_record = get_last_record_number()
    data["No.Registro"] = last_record + 1

    # Timestamp
    data["Fecha"] = datetime.now().strftime("%d-%m-%Y")   # Here is the format of datetime

    # Call the backend function to register the entry
    register_entry(data)

    # Display success message in the GUI
    success_message = ctk.CTkLabel(frame, text="Asistencia registrada con éxito", fg_color=colors["green"], font=("Arial", 12, "bold"))
    success_message.grid(row=len(entries) + len(time_entries) + 3, column=0, columnspan=2, pady=10)

    # Automatically clear the message after a short delay
    frame.after(3000, success_message.destroy)  # Clears message after 3 seconds

