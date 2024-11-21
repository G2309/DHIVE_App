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
def verify_user(carnet):
    df = get_users_data()
    # Convertir el carnet a un número para la comparación
    try:
        carnet = int(carnet.strip())
    except ValueError:
        return False  # Si no es un número, retorna False

    user = df[df["Carnet"] == carnet]  # Buscar por carnet numérico
    return not user.empty  # Retorna True si existe; False si no existe


# Search a user by carnet
def find_user_by_id(carnet):
    df = get_users_data()
    return df[df['Carnet'] == carnet]

# Modify data
def update_user_in_excel(modified_user):
    df = get_users_data()
    try:
        carnet = int(modified_user["Carnet"])
    except ValueError:
        return False  # If carnet is invalid, return False

    # Find the user index
    user_index = df[df["Carnet"] == carnet].index
    if len(user_index) > 0:
        index = user_index[0]  # Get the first match index
        for column, value in modified_user.items():
            if column in df.columns:
                df.at[index, column] = value  # Update the specific column

        # Save changes back to the Excel file
        df.to_excel("DATOS_USUARIOS.xlsx", index=False)
        return True
    else:
        return False

def get_trainings(training_num):
    if isinstance(training_num, str):
        number = [int(n) for n in training_num.split(',') if n.isdigit()]
    else:
        number = []
    return ', '.join([trainings_available[num] for num in number if num in trainings_available])
