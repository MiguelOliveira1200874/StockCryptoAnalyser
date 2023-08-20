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
