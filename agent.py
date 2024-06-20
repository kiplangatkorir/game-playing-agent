import numpy as np
import random

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def get_state_key(self, state):
        return str(state.reshape(3 * 3))

    def choose_action(self, state, available_actions):
        state_key = self.get_state_key(state)
        if np.random.uniform(0, 1) < self.epsilon:
            return random.choice(available_actions)
        q_values = self.q_table.get(state_key, {})
        max_q = max(q_values.values()) if q_values else 0
        best_actions = [action for action, q in q_values.items() if q == max_q]
        return random.choice(best_actions) if best_actions else random.choice(available_actions)

    def update_q_table(self, state, action, reward, next_state):
        state_key = self.get_state_key(state)
        next_state_key = self.get_state_key(next_state)
        if state_key not in self.q_table:
            self.q_table[state_key] = {}
        if action not in self.q_table[state_key]:
            self.q_table[state_key][action] = 0
        max_next_q = max(self.q_table.get(next_state_key, {}).values(), default=0)
        self.q_table[state_key][action] += self.alpha * (reward + self.gamma * max_next_q - self.q_table[state_key][action])
