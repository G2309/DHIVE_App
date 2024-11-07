from app.file_reader import read_user_data
import pandas as pd

# Diccionario con las capacitaciones disponibles (para agregar una nueva capacitacion, hazlo en el ultimo lugar sumando 1 a la llave)
trainings_available = {
        1: "Láser K40",
        2: "Láser ULS",
        3: "Escaner 3D Mano",
        4: "Escaner 3D Pequeño",
        5: "Impresión 3D",
        6: "Impresión 3D resina",
        7: "Máquina de coser",
        8: "Seguridad",
        9: "Sublimanción",
        10: "Termoformadora",
        11: "Vinilo",
        12: "Impresión 3D fibra carbono",
        13: "Taladro de pedestal",
        14: "Laminadora",
        15: "Dobladora"
}

# Leer todos los datos
def get_users_data():
    return read_user_data()

# Agregar un nuevo usuario
def add_new_user(new_user):
    df = get_users_data()
    new_user["Número usuario"] = df["Número usuario"].max() + 1
    df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
    df.to_excel('DATOS_USUARIOS.xlsx', index=False)
    return True

# Verificar si un usuario existe en el xlsx
def verify_user(name, carnet):
    df = get_users_data()
    user = df[(df["Primer Nombre"] == name) & (df["Carnet"] == carnet)]
    return not user.empty   # Retorna True si existe; False si no existe

# Buscar por carnet
def find_user_by_id(carnet):
    df = get_users_data()
    return df[df['Carnet'] == carnet]

# MModificar data
def update_user_data(carnet, new_data):
    df = get_users_data()
    index = df[df['Carnet'] == carnet].index
    if not index.empty:
        df.loc[index, new_data.keys()] = new_data.values()
        df.to_excel('DATOS_USUARIOS.xlsx', index=False)
        return True
    return False

def get_trainings(training_num):
    number = [int(n) for n in training_num.split(',') if n.isdigit()]
    return ', '.join([trainings_available[num] for num in number if num in trainings_available])

