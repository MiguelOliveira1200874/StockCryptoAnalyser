# Main entry point of our application
from test import test_application
from data_preprocessing import preprocess_data
from interface import create_interface
from visualization import visualize_data

if __name__ == "__main__":
    # Create the user interface and get the symbol from the user
    symbol = create_interface()

    from data_fetching import fetch_data

    # Check if the symbol is for a stock or a cryptocurrency
    if symbol in ["AAPL", "MSFT", "GOOGL", "AMZN", "FB"]:  # Add more stock symbols as needed
        # Fetch and preprocess stock data
        data = fetch_data(symbol, "TIME_SERIES_DAILY")
        if data is None:
            print("Error fetching stock data. Exiting program.")
            exit(1)
    else:
        # Fetch and preprocess crypto data
        data = fetch_data(symbol, "DIGITAL_CURRENCY_DAILY")
        if data is None:
            print("Error fetching crypto data. Exiting program.")
            exit(1)

    preprocessed_data = preprocess_data(data)
    visualize_data(preprocessed_data, symbol)
