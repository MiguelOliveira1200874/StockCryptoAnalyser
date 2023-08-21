# Functions for data cleaning and preprocessing
def preprocess_data(data):
    # Ensure 'date' column is present
    if 'date' not in data.columns:
        print("Error: 'date' column not found in data.")
        return None

    # Remove any rows with missing 'date' data
    data = data.dropna(subset=['date'])

    # Convert data types if necessary
    # data = data.astype({'column_name': 'data_type'})

    # Normalize the data if necessary
    # data = (data - data.min()) / (data.max() - data.min())

    return data
