# Functions for technical analysis
import numpy as np

def calculate_moving_average(data, window_size):
    return data['4a. close (USD)'].rolling(window=window_size).mean()

def calculate_support_resistance(data, window_size):
    support = data['4a. close (USD)'].rolling(window=window_size).min()
    resistance = data['4a. close (USD)'].rolling(window=window_size).max()
    return support, resistance

def analyze_data(data):
    # Calculate the moving average with a window size of 20
    data['Moving Average'] = calculate_moving_average(data, 20)

    # Calculate the support and resistance levels with a window size of 20
    data['Support'], data['Resistance'] = calculate_support_resistance(data, 20)

    return data
