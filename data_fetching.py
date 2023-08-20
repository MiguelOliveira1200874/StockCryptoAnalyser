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
        "apikey": "MRA4JAKP2W181V2P"
    }

    if function_name == "DIGITAL_CURRENCY_DAILY":
        params["market"] = "USD"

    # Print the parameters and send a GET request to the API
    print(params)
    response = requests.get(url, params=params)

    # If the request failed, print an error message and return None
    if response.status_code != 200:
        print(f"Error fetching data for {symbol}: {response.status_code}")
        return None

    # Convert the response to JSON and print the response
    json_response = response.json()
    print(json_response)

    # Extract the time series data from the JSON response
    if function_name == "TIME_SERIES_DAILY":
        time_series_key = "Time Series (Daily)"
    elif function_name == "DIGITAL_CURRENCY_DAILY":
        time_series_key = "Time Series (Digital Currency Daily)"
    else:
        print(f"Error: Invalid function name '{function_name}'.")
        return None

    if time_series_key not in json_response:
        print(f"Error: The key '{time_series_key}' was not found in the JSON response.")
        return None

    time_series_data = json_response[time_series_key]

    # Convert the time series data to a pandas DataFrame and clean it
    data = pd.DataFrame(time_series_data)
    # TODO: Add data cleaning code here

    # Pause to avoid hitting the API rate limit
    time.sleep(12)

    return data
