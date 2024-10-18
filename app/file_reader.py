# File reader 

import pandas as pd

# XLSX containing students information (name, lastname, id, etc...)
def read_user_data(file_path="DATOS_USUARIOS.xlsx"):
    return pd.read_excel(file_path)

# XLSX containing the name of trainings available
def read_training_data(file_path="Capacitaciones.xlsx"):
    return pd.read_excel(file_path)

# XLSX with aux attendance
def read_aux_data(file_path="Entradas_Auxiliares.xlsx"):
    return pd.read_excel(file_path)

# XLSX with students attendance
def read_attendance_data(file_path="Registro_entradas.xlsx"):
    return pd.read_excel(file_path)
