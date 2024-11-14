from app.file_reader import read_user_data, read_training_data
import pandas as pd

# Read Capacitaciones.xlsx and save to dict
def load_trainings_available():
    df = read_training_data()
    return dict(zip(df['No.Capacitación'].astype(int), df['Capacitación']))

trainings_available = load_trainings_available()

# Read users data
def get_users_data():
    return read_user_data()

# Add a new user to xlsx
def add_new_user(new_user):
    df = get_users_data()
    new_user["Número usuario"] = df["Número usuario"].max() + 1
    df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
    df.to_excel('DATOS_USUARIOS.xlsx', index=False)
    return True

# Verify if a user exists in the xlsx
def verify_user(name, carnet):
    df = get_users_data()
    user = df[(df["Primer Nombre"] == name) & (df["Carnet"] == carnet)]
    return not user.empty   # Retorna True si existe; False si no existe

# Search a user by carnet
def find_user_by_id(carnet):
    df = get_users_data()
    return df[df['Carnet'] == carnet]

# Modify data
def update_user_data(carnet, new_data):
    df = get_users_data()
    index = df[df['Carnet'] == carnet].index
    if not index.empty:
        df.loc[index, new_data.keys()] = new_data.values()
        df.to_excel('DATOS_USUARIOS.xlsx', index=False)
        return True
    return False

def get_trainings(training_num):
    if isinstance(training_num, str):
        number = [int(n) for n in training_num.split(',') if n.isdigit()]
    else:
        number = []
    return ', '.join([trainings_available[num] for num in number if num in trainings_available])
