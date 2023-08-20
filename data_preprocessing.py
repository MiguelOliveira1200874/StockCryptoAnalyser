# Functions for data cleaning and preprocessing
def preprocess_data(data):
    # Remove any rows with missing data
    data = data.dropna(subset=['date'])

    # Ensure 'date' column is kept
    if 'date' not in data.columns:
        print("Error: 'date' column not found in data.")
        return None

    # Convert data types if necessary
    # data = data.astype({'column_name': 'data_type'})

    # Normalize the data if necessary
    # data = (data - data.min()) / (data.max() - data.min())

    return data
