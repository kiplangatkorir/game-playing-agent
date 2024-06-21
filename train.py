import numpy as np

class QLearningAgent:
    def __init__(self, num_actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = np.zeros(num_actions)

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.exploration_rate:
            return np.random.choice(self.num_actions)
        else:
            return np.argmax(self.q_table)

    def update_q_table(self, state, action, reward, next_state):
        # Update Q-value for the chosen action
        self.q_table[action] += self.learning_rate * (
            reward + self.discount_factor * np.max(self.q_table) - self.q_table[action]
        )

# Example usage
if __name__ == "__main__":
    agent = QLearningAgent(num_actions=4)  # Assuming 4 actions (up, down, left, right)
    state = (0, 0)  # Example state (current position)
    action = agent.choose_action(state)
    print("Chosen action:", action)
    next_state = (0, 1)  # Example next state after action
    reward = 0.0  # Example reward
    agent.update_q_table(state, action, reward, next_state)
    print("Updated Q-table:", agent.q_table)
