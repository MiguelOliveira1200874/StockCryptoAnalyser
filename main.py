# Main entry point of our application
from test import test_application
from data_preprocessing import preprocess_data
from interface import create_interface
from visualization import visualize_data

if __name__ == "__main__":
    # Create the user interface and get the symbol from the user
    symbol = create_interface()

    # Fetch and preprocess stock data
    stock_data = test_application(symbol)
    preprocessed_stock_data = preprocess_data(stock_data)
    visualize_data(preprocessed_stock_data, symbol)

    # Fetch and preprocess crypto data
    crypto_data = test_application(symbol)
    preprocessed_crypto_data = preprocess_data(crypto_data)
    visualize_data(preprocessed_crypto_data, symbol)
