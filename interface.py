# Code for the user interface
def create_interface(agent, env):
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
