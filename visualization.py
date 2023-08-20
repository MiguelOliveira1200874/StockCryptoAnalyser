import matplotlib.pyplot as plt

# Functions for data visualization
import io
import base64
import urllib

def visualize_data(data, symbol):
    # Extract the closing prices
    if '4a. close (USD)' in data.columns:
        closing_prices = data['4a. close (USD)']
    elif '4. close' in data.columns:
        closing_prices = data['4. close']
    else:
        print("Error: The DataFrame does not contain a closing prices column.")
        return None

    # Create a plot
    plt.figure(figsize=(10, 5))
    plt.plot(closing_prices)
    plt.title(f'Closing Prices of {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)

    # Convert the plot to a PNG image
    png_image = io.BytesIO()
    plt.savefig(png_image, format='png')
    png_image.seek(0)

    # Encode the PNG image to base64
    png_image_base64 = base64.b64encode(png_image.read())
    return urllib.parse.quote(png_image_base64)
