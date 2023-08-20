# Code for the user interface
def get_indicators():
    print("Please select the indicators you want to see:")
    print("1. Moving Average")
    print("2. Support and Resistance")
    print("3. Important Levels")
    print("4. RSI")
    print("5. MACD")
    print("6. Bollinger Bands")
    print("Enter the numbers of the indicators you want to see, separated by commas:")
    indicators = input().strip().split(',')
    return indicators

def create_interface(agent, env, data):
    print("Welcome to the Stocks and Crypto Analyzer!")
    while True:
        print("Please enter the symbol of the stock or cryptocurrency you want to analyze:")
        symbol = input().strip()
        if symbol:  # basic check to ensure the input is not empty
            state = env.reset()
            action = agent.choose_action(state)
            if action == 0:  # Buy
                print("Buy at current price")
            elif action == 1:  # Sell
                print("Sell at current price")
            else:
                print("Hold at current price")
            indicators = get_indicators()
            display_important_levels(data, indicators)
            return symbol
        else:
            print("Invalid input. Please try again.")

def get_decision(agent, state):
    action = agent.choose_action(state)
    if action == 0:  # Buy
        return "Buy at current price"
    elif action == 1:  # Sell
        return "Sell at current price"
    else:
        return "Hold at current price"

def display_important_levels(data, indicators):
    print("Selected Indicators:")
    for indicator in indicators:
        if indicator == '1':
            print("Moving Average:")
            print(data['Moving Average'])
        elif indicator == '2':
            print("Support and Resistance:")
            print(data['Support'], data['Resistance'])
        elif indicator == '3':
            print("Important Levels:")
            print(data['Important Levels'])
        elif indicator == '4':
            print("RSI:")
            print(data['RSI'])
        elif indicator == '5':
            print("MACD:")
            print(data['MACD'])
        elif indicator == '6':
            print("Bollinger Bands:")
            print(data['Bollinger Bands'])
