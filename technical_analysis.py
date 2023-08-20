# Functions for technical analysis
import numpy as np
from collections import Counter

def calculate_moving_average(data, window_size):
    return data['4a. close (USD)'].rolling(window=window_size).mean()

def calculate_support_resistance(data, window_size):
    support = data['4a. close (USD)'].rolling(window=window_size).min()
    resistance = data['4a. close (USD)'].rolling(window=window_size).max()
    return support, resistance

def detect_important_levels(data, num_levels):
    # Round the closing prices to the nearest whole number
    rounded_prices = data['4a. close (USD)'].round()

    # Calculate the frequency of each price level
    price_counts = Counter(rounded_prices)

    # Select the price levels with the highest frequencies
    important_levels = [price for price, count in price_counts.most_common(num_levels)]

    return important_levels

def analyze_data(data):
    # Calculate the moving average with a window size of 20
    data['Moving Average'] = calculate_moving_average(data, 20)

    # Calculate the support and resistance levels with a window size of 20
    data['Support'], data['Resistance'] = calculate_support_resistance(data, 20)

    # Detect the most important levels
    data['Important Levels'] = detect_important_levels(data, 5)

    # Calculate the technical indicators
    data['RSI'] = calculate_rsi(data)
    data['MACD'] = calculate_macd(data)
    data['Bollinger Bands'] = calculate_bollinger_bands(data)

    return data
def calculate_rsi(data, period=14):
    delta = data['4a. close (USD)'].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    average_gain = up.rolling(window=period).mean()
    average_loss = abs(down.rolling(window=period).mean())
    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
def calculate_macd(data, short_period=12, long_period=26, signal_period=9):
    short_ema = data['4a. close (USD)'].ewm(span=short_period, adjust=False).mean()
    long_ema = data['4a. close (USD)'].ewm(span=long_period, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    macd = macd_line - signal_line
    return macd
def calculate_bollinger_bands(data, window_size=20, num_of_std=2):
    rolling_mean = data['4a. close (USD)'].rolling(window=window_size).mean()
    rolling_std = data['4a. close (USD)'].rolling(window=window_size).std()
    upper_band = rolling_mean + (rolling_std * num_of_std)
    lower_band = rolling_mean - (rolling_std * num_of_std)
    return upper_band, lower_band
