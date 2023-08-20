# Code for the user interface
def create_interface():
    print("Welcome to the Stocks and Crypto Analyzer!")
    while True:
        print("Please enter the symbol of the stock or cryptocurrency you want to analyze:")
        symbol = input().strip()
        if symbol:  # basic check to ensure the input is not empty
            return symbol
        else:
            print("Invalid input. Please try again.")
