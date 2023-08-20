import numpy as np

class QLearningAgent:
    def __init__(self, action_space, learning_rate=0.01, discount_factor=0.99, exploration_rate=1.0, exploration_decay_rate=0.001):
        self.action_space = action_space
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay_rate = exploration_decay_rate
        self.q_table = {}

    def choose_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return self.action_space.sample()
        else:
            return np.argmax(self.q_table.get(state, np.zeros(self.action_space.n)))

    def learn(self, state, action, reward, next_state, done):
        old_value = self.q_table.get(state, np.zeros(self.action_space.n))[action]
        next_max = np.max(self.q_table.get(next_state, np.zeros(self.action_space.n)))

        new_value = (1 - self.learning_rate) * old_value + self.learning_rate * (reward + self.discount_factor * next_max)
        new_values = self.q_table.get(state, np.zeros(self.action_space.n))
        new_values[action] = new_value
        self.q_table[state] = new_values

        if done:
            self.exploration_rate *= np.exp(-self.exploration_decay_rate)
