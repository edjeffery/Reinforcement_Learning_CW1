# For example, the following np.array 'policy' defined below has the correct format
# (but really is just a random collection of directions).
import numpy as np
from Gridworld import Gridworld
policy = np.array(["n", "w", "s", "w", "e", "n", "w", "s", "w", "e", "n", "w", "s", "w", "e", "n", "w", "s", "w", "e", "n", "w", "s", "w", "e"])
print(type(policy))
print(policy.shape)

# The following np.array 'v' has the correct format (but is just a random
# collection of floats).
#v = np.random.rand(25)
#print(v)

# Please write your code for Exercise 1 here. We will mark your coursework by checking
# the values of the variables policy and v in this cell. Your code should compute the
# values of policy and v from scratch when this cell is executed, using the value
# iteration algorithm.

theta = 1e-10
gamma = 1
epsilon = 0
alpha = 0

env = Gridworld()

v = np.zeros(25)
#print(v)

lookup_table = np.zeros((25,4), dtype=np.ndarray)

actions = env.get_available_actions()
print(actions)

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
        #print(list)

#print(lookup_table)
#print("")
#print(lookup_table[13][2])


def look_ahead(s, v):
    action_values = np.zeros(4)
    for action in range(4):
        for p, new_state, r in lookup_table[s][action]:
            #print(p, new_state, r)
            action_values[action] += p * (r + gamma * v[new_state])
    #print(action_values)
    return action_values


while True:
    delta = 0

    for state in range(25):
        if not env.is_terminal(state):
            #print("state = " + str(state))
            action_values = look_ahead(state, v)
            best_action_value = np.max(action_values)
            best_action = actions[np.argmax(action_values)]
            #print(best_action)
            #print("Best action value = " + str(best_action_value))
            #print("v[state] = " + str(v[state]))
            #print("delta = " + str(delta))
            delta = max(delta, np.abs(best_action_value - v[state]))
            #print("new delta = " + str(delta))
            v[state] = best_action_value
            policy[state] = best_action
            #print(delta)

    if delta < theta:
        #print("break")
        break

    #print("\nNext iteration\n")

print(v)
print(policy)
