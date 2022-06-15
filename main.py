import agent
import environment
import policy
import numpy as np

bandit = agent.DateBandit(mode='winloss')
n_trials = 550
n_experiments = 500


# This is an example.
agents = [  agent.Agent(bandit, policy.RandomPolicy()),
            agent.Agent(bandit, policy.EpsilonGreedyPolicy(0)),
            agent.Agent(bandit, policy.EpsilonGreedyPolicy(.2)),
            #agent.Agent(bandit, policy.EpsilonGreedyPolicy(.02)),
            agent.Agent(bandit, policy.UCBPolicy(1)),
            #agent.Agent(bandit, policy.UCBPolicy(2)),
            agent.Agent(bandit, policy.UCBPolicy(5))]

# agents = [agent.Agent(bandit, policy.EpsilonGreedyPolicy(i)) for i in np.linspace(0.001, 0.9, 5)]
agents = [agent.Agent(bandit, policy.EpsilonGreedyPolicy(0.2))]

env = environment.Environment(bandit, agents)
scores, optimal = env.run(n_trials, n_experiments)
env.plot_results(scores, optimal)
