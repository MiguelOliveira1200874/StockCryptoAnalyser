import os
import time
import requests
import pandas as pd

# Function to fetch data from APIs
def fetch_data(symbol, function_name):
    # URL of the Alpha Vantage API endpoint
    url = "https://www.alphavantage.co/query"

    # Parameters for the API request
    params = {
        "function": function_name,
        "symbol": symbol,
        "apikey": os.getenv("ALPHA_VANTAGE_API_KEY")
    }

    if function_name == "DIGITAL_CURRENCY_DAILY":
        params["market"] = "USD"

    # Send a GET request to the API
    response = requests.get(url, params=params)

    # If the request failed, print an error message and return None
    if response.status_code != 200:
        print(f"Error fetching data for {symbol}: {response.status_code}")
        return None

    # Convert the response to JSON
    json_response = response.json()

    # Extract the time series data from the JSON response
    time_series_key = "Time Series (Daily)" if "Time Series (Daily)" in json_response else "Time Series (Digital Currency Daily)"
    time_series_data = json_response[time_series_key]

    # Convert the time series data to a pandas DataFrame and clean it
    data = pd.DataFrame(time_series_data)
    # TODO: Add data cleaning code here

    # Pause to avoid hitting the API rate limit
    time.sleep(12)

    return data
