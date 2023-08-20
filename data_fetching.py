import os
import time
import requests
import pandas as pd

# Function to fetch data from APIs
def fetch_data(symbol, function_name, currency):
    # URL of the Alpha Vantage API endpoint
    url = "https://www.alphavantage.co/query"

    # Parameters for the API request
    params = {
        "function": function_name,
        "symbol": symbol,
        "apikey": "MRA4JAKP2W181V2P",
        "interval": "daily",
        "time_period": "10",
        "series_type": "close"
    }

    if function_name == "DIGITAL_CURRENCY_DAILY":
        params["market"] = currency

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

    # Convert the time series data to a pandas DataFrame with 'date' and '4a. close (USD)' columns
    data = pd.DataFrame.from_dict(time_series_data, orient='index')
    data.reset_index(inplace=True)
    if function_name == "TIME_SERIES_DAILY":
        data.columns = ['date', '1. open', '2. high', '3. low', '4. close', '5. volume']
        data['4. close'] = data['4. close'].astype(float)
    elif function_name == "DIGITAL_CURRENCY_DAILY":
        data.columns = ['date', '1a. open (USD)', '1b. open (native)', '2a. high (USD)', '2b. high (native)', '3a. low (USD)', '3b. low (native)', '4a. close (USD)', '4b. close (native)', '5. volume', '6. market cap (USD)']
        data['4a. close (USD)'] = data['4a. close (USD)'].astype(float)
    data['date'] = pd.to_datetime(data['date'])
    data = data.sort_values(by='date')
    data.reset_index(drop=True, inplace=True)

    # Pause to avoid hitting the API rate limit
    time.sleep(12)

    return data
