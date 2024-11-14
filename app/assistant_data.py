# assistants_data.py

import pandas as pd
from datetime import datetime

def add_new_schedule_entry(first_name, second_name, first_surname, second_surname, carnet, entry_time, file_path="Entradas_Auxiliares.xlsx"):
    """
    Adds a new schedule entry for an assistant into the Excel file.
    
    Parameters:
        first_name (str): First name of the assistant.
        second_name (str): Second name of the assistant.
        first_surname (str): First surname of the assistant.
        second_surname (str): Second surname of the assistant.
        carnet (int): ID number of the assistant.
        entry_time (str): Entry time in HH:MM:SS format.
        file_path (str): Path to the Excel file.
    
    Returns:
        bool: True if entry added successfully, False otherwise.
    """
    try:
        # Read the current Excel file
        df = pd.read_excel(file_path)
        
        # Create a new entry with current date
        new_entry = {
            "No.Registro": len(df) + 1,
            "Primer nombre": first_name,
            "Segundo nombre": second_name,
            "Primer apellido": first_surname,
            "Segundo apellido": second_surname,
            "Carnet": carnet,
            "Hora entrada": entry_time,
            "Hora salida": None,  # No salida initially
            "Fecha": datetime.now().date()
        }
        
        # Append the new entry
        df = df.append(new_entry, ignore_index=True)
        
        # Save back to the Excel file
        df.to_excel(file_path, index=False)
        return True
    except Exception as e:
        print("Error adding new schedule entry:", e)
        return False

def register_entry(data):
    """
    Registers a new entry in the Excel file with attendance records.
    """
    # Load current data
    file_path = "Entradas_Auxiliares.xlsx"
    df = pd.read_excel(file_path)
    
    # Append new row
    new_entry = pd.DataFrame([data])
    df = pd.concat([df, new_entry], ignore_index=True)
    
    # Save updated data back to Excel
    df.to_excel(file_path, index=False)

def get_last_record_number(file_path='Entradas_Auxiliares.xlsx'):
    """
    Retrieves the last 'No.Registro' value from the Excel file and returns it.
    """
    # Leer el archivo Excel
    try:
        df = pd.read_excel(file_path)
        
        # Obtener la última fila de la columna 'No.Registro'
        if not df.empty:
            last_record = df['No.Registro'].max()
        else:
            last_record = 0  # Si el archivo está vacío, empezamos desde 0
        
        return last_record
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return 0
