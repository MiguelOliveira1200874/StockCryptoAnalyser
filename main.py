# Main entry point of our application
from test import test_application
from data_preprocessing import preprocess_data
from interface import create_interface, get_decision
from visualization import visualize_data
from predictive_analysis import TradingEnv
from agent import QLearningAgent

if __name__ == "__main__":
    from data_fetching import fetch_data

    # Check if the symbol is for a stock or a cryptocurrency
    if symbol in ["AAPL", "MSFT", "GOOGL", "AMZN", "FB"]:  # Add more stock symbols as needed
        # Fetch and preprocess stock data
        data = fetch_data(symbol, "TIME_SERIES_DAILY")
        if data is None:
            print("Error fetching stock data. Exiting program.")
            exit(1)
    else:
        # Fetch and preprocess crypto data
        data = fetch_data(symbol, "DIGITAL_CURRENCY_DAILY")
        if data is None:
            print("Error fetching crypto data. Exiting program.")
            exit(1)

    preprocessed_data = preprocess_data(data)

    # Initialize the trading environment and the agent
    env = TradingEnv(preprocessed_data)
    agent = QLearningAgent(env.action_space)

    # Train the agent
    num_episodes = 1000
    for episode in range(num_episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done, info = env.step(action)
            agent.learn(state, action, reward, next_state, done)
            state = next_state

    # Create the user interface and get the symbol from the user
    symbol = create_interface(agent, env, preprocessed_data)

    # Create the user interface and get the symbol from the user
    symbol = create_interface(agent, env, preprocessed_data)

    from data_fetching import fetch_data

    # Check if the symbol is for a stock or a cryptocurrency
    if symbol in ["AAPL", "MSFT", "GOOGL", "AMZN", "FB"]:  # Add more stock symbols as needed
        # Fetch and preprocess stock data
        data = fetch_data(symbol, "TIME_SERIES_DAILY")
        if data is None:
            print("Error fetching stock data. Exiting program.")
            exit(1)
    else:
        # Fetch and preprocess crypto data
        data = fetch_data(symbol, "DIGITAL_CURRENCY_DAILY")
        if data is None:
            print("Error fetching crypto data. Exiting program.")
            exit(1)

    preprocessed_data = preprocess_data(data)

    # Initialize the trading environment and the agent
    env = TradingEnv(preprocessed_data)
    agent = QLearningAgent(env.action_space)

    # Train the agent
    num_episodes = 1000
    for episode in range(num_episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done, info = env.step(action)
            agent.learn(state, action, reward, next_state, done)
            state = next_state

    # Use the trained agent to make predictions
    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(state)
        if action == 0:  # Buy
            print("Buy at current price")
        elif action == 1:  # Sell
            print("Sell at current price")
        next_state, reward, done, info = env.step(action)
        state = next_state
