import random
from environment import TicTacToe
from agent import QLearningAgent

def train_agent(episodes=10000):
    env = TicTacToe()
    agent = QLearningAgent()
    for episode in range(episodes):
        state = env.reset()
        done = False
        while not done:
            available_actions = env.available_actions()
            action = agent.choose_action(state, available_actions)
            print(f"Chosen action: {action}, Available actions: {available_actions}")  # Debug print
            try:
                next_state, done, winner = env.step(action, 1)
            except Exception as e:
                print(f"Exception during step: {e}")
                break
            if done:
                reward = 1 if winner == 1 else 0
            else:
                opp_action = random.choice(env.available_actions())
                print(f"Opponent action: {opp_action}")  # Debug print
                try:
                    next_state, done, winner = env.step(opp_action, -1)
                except Exception as e:
                    print(f"Exception during opponent step: {e}")
                    break
                reward = -1 if done and winner == -1 else 0
            agent.update_q_table(state, action, reward, next_state)
            state = next_state
            env.render()  # Print board state after each step (optional)
    return agent

if __name__ == "__main__":
    agent = train_agent()
    print("Training completed.")
