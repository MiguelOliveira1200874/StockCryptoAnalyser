import plotly.graph_objects as go
import plotly.offline as pyo

# Functions for data visualization

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
    fig = go.Figure(data=[go.Scatter(x=closing_prices.index, y=closing_prices, mode='lines', name='closing prices')])
    fig.update_layout(title=f'Closing Prices of {symbol}', xaxis_title='Date', yaxis_title='Price')

    # Return the plot as HTML
    return pyo.plot(fig, output_type='div')
