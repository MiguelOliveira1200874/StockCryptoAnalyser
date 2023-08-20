import matplotlib.pyplot as plt

# Functions for data visualization
def visualize_data(data, symbol):
    # Extract the closing prices
    closing_prices = data['4. close']

    # Create a plot
    plt.figure(figsize=(10, 5))
    plt.plot(closing_prices)
    plt.title(f'Closing Prices of {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()
