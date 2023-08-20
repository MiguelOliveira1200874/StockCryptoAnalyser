# Functions for data cleaning and preprocessing
def preprocess_data(data):
    # Remove any rows with missing data
    data = data.dropna()

    # Convert data types if necessary
    # data = data.astype({'column_name': 'data_type'})

    # Normalize the data if necessary
    # data = (data - data.min()) / (data.max() - data.min())

    return data
