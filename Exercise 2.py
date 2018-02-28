import numpy as np
from Gridworld import Gridworld
policy = np.array(["n", "w", "s", "w", "e", "n", "w", "s", "w", "e", "n", "w", "s", "w", "e", "n", "w", "s", "w", "e", "n", "w", "s", "w", "e"])

# Please write your code for Exercise 1 here. We will mark your coursework by checking
# the values of the variables policy and v in this cell. Your code should compute the
# values of policy and v from scratch when this cell is executed, using the value
# iteration algorithm.

theta = 1e-10
gamma = 1
epsilon = 0
alpha = 0.2

env = Gridworld()
v = np.zeros(25)
actions = env.get_available_actions()

# Set up the lookup table that stores a list of tuples containing probability, next state and reward for every state-action pair
lookup_table = np.zeros((25,4), dtype=np.ndarray)
for state in range(25):
    for action in actions:
        list = []
        for a in actions:
            if a == action:
                prob = (1-alpha) + alpha / len(actions)
            else:
                prob = alpha / len(actions)
            (new_state, reward) = env.make_step(state, a)
            list.append((prob, new_state, reward))
        lookup_table[state][actions.index(action)] = list


# Computes one-step look ahead from a state to get the action-values of performing each action
def look_ahead(s, v):
    action_values = np.zeros(4)
    for action in range(4):
        for p, new_state, r in lookup_table[s][action]:
            action_values[action] += p * (r + gamma * v[new_state])
    print(state, action_values)
    return action_values

# Iterates until the change between old and new V(s) values is sufficiently small
while True:
    delta = 0

    for state in range(25):
        if not env.is_terminal(state):
            action_values = look_ahead(state, v)
            best_action_value = np.max(action_values)
            best_action = actions[np.argmax(action_values)]
            delta = max(delta, np.abs(best_action_value - v[state]))
            v[state] = best_action_value
            policy[state] = best_action
    print(delta)
    if delta < theta:
        break

# Print out the state-values
print(v)
# Print out the optimal policy
print(policy)
