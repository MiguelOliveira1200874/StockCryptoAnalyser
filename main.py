# Main entry point of our application
from test import test_application
from data_preprocessing import preprocess_data
from interface import create_interface
from visualization import visualize_data

if __name__ == "__main__":
    # Create the user interface and get the symbol from the user
    symbol = create_interface()

    from data_fetching import fetch_data

    # Fetch and preprocess stock data
    stock_data = fetch_data(symbol, "TIME_SERIES_DAILY")
    preprocessed_stock_data = preprocess_data(stock_data)
    visualize_data(preprocessed_stock_data, symbol)

    # Fetch and preprocess crypto data
    crypto_data = fetch_data(symbol, "DIGITAL_CURRENCY_DAILY")
    preprocessed_crypto_data = preprocess_data(crypto_data)
    visualize_data(preprocessed_crypto_data, symbol)
