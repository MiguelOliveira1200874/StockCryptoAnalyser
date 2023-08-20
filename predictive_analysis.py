import gym
from gym import spaces
import numpy as np

# Functions for predictive analysis

class TradingEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self, df):
        super(TradingEnv, self).__init__()

        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions, Box for continuous action
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(n,), dtype=np.float32)

        # Load data from a pandas dataframe
        self.df = df
        self.reward_range = (-np.inf, np.inf)

    def step(self, action):
        # Execute one time step within the environment
        pass

    def reset(self):
        # Reset the state of the environment to an initial state
        self.current_step = 0
        self.total_reward = 0.0
        self.done = False
        return self._get_observation()

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        if self.done:
            print(f"Info: {self.total_reward}")
        else:
            print(f"Day: {self.current_step}, Price: {self.df.loc[self.current_step, '4a. close (USD)']}")
