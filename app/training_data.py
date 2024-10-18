from app.file_reader import read_training_data

# Get all data
def get_training_data():
    return read_training_data()

# Add new training records
def add_training_record(new_record):
    df = get_training_data()
    df - df.append(new_record, ignore_index=True)
    df.to_excel('../Capacitaciones.xlsx', index=False)
