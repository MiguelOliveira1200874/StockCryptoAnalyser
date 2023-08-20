import gym
from gym import spaces
import numpy as np

# Functions for predictive analysis

class TradingEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self, df, initial_balance=10000):
        super(TradingEnv, self).__init__()

        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions, Box for continuous action
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(df.shape[1],), dtype=np.float32)

        # Load data from a pandas dataframe
        self.df = df
        self.reward_range = (-np.inf, np.inf)

        # Initialize additional attributes
        self.initial_balance = initial_balance
        self.balance = self.initial_balance
        self.shares = 0

    def step(self, action):
        # Execute one time step within the environment
        self.current_step += 1

        # Get the current price from the dataframe
        current_price = self.df.loc[self.current_step, '4a. close (USD)']

        # Execute the action and update the balance and shares
        if action == 0:  # Buy
            if self.balance > current_price:
                self.balance -= current_price
                self.shares += 1
        elif action == 1:  # Sell
            if self.shares > 0:
                self.balance += current_price
                self.shares -= 1
        # action 2 means 'Hold', so we do nothing

        # Calculate the reward
        reward = self.balance - self.initial_balance
        self.total_reward += reward

        # Check if we're done
        if self.current_step >= len(self.df):
            self.done = True

        return self._get_observation(), reward, self.done, {}

    def reset(self):
        # Reset the state of the environment to an initial state
        self.current_step = 0
        self.total_reward = 0.0
        self.done = False
        self.balance = self.initial_balance
        self.shares = 0
        return self._get_observation()

    def _get_observation(self):
        # Return the current observation
        return self.df.loc[self.current_step]

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        if self.done:
            print(f"Info: {self.total_reward}")
        else:
            print(f"Day: {self.current_step}, Price: {self.df.loc[self.current_step, '4a. close (USD)']}")
