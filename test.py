# Test cases for our application
from data_fetching import fetch_stock_data, fetch_crypto_data

def test_application():
    # Test the fetch_stock_data function
    stock_data = fetch_stock_data("AAPL")
    print(stock_data)

    # Test the fetch_crypto_data function
    crypto_data = fetch_crypto_data("BTC")
    print(crypto_data)
