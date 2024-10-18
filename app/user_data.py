from file_reader import read_user_data

# Get all data
def get_users_data():
    return read_user_data()

# Add a new student/aux to db
def add_new_user(new_user):
    df = get_users_data()
    df = df.append(new_user, ignore_index=True)
    df.to_excel('../DATOS_USUARIOS.xlsx', index=False)

# Find user by ID
def find_user_by_id(carne):
    df = get_users_data()
    return df[df['Carnet'] == carne]

# Modify user data
def update_user_data(carne, new_data):
    df = get_users_data()
    index = df[df['Carnet'] == carne].index
    if not index.empty:
        df.loc[index, new_data.keys()] = new_data.values()
        df.to_excel('DATOS_USUARIOS.xlsx', index=False)
        return True
    return False

