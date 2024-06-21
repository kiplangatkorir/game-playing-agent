from environment import RobotEnvironment
from agent import QLearningAgent  # Import your trained agent class here

def evaluate_agent(env, agent, episodes=10):
    total_rewards = 0.0
    steps_per_episode = []

    for episode in range(episodes):
        state = env.reset()
        episode_reward = 0.0
        step = 0
        done = False

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            episode_reward += reward
            state = next_state
            step += 1

        total_rewards += episode_reward
        steps_per_episode.append(step)
        print(f"Episode {episode + 1}: Total Reward = {episode_reward}, Steps = {step}")

    avg_reward = total_rewards / episodes
    avg_steps = sum(steps_per_episode) / episodes
    print(f"\nAverage Reward over {episodes} episodes: {avg_reward}")
    print(f"Average Steps per episode: {avg_steps}")

# Example usage
if __name__ == "__main__":
    env = RobotEnvironment()
    agent = QLearningAgent(num_actions=4)  # Assuming 4 actions (up, down, left, right)
    # Load your trained agent here if available
    # agent.load_model("path/to/your/trained_model.pth") 

    evaluate_agent(env, agent, episodes=10)
