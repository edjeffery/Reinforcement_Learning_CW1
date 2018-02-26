# For example, the following np.array 'policy' defined below has the correct format
# (but really is just a random collection of directions).
import numpy as np
policy = np.array(["n", "w", "s", "w", "e", "n", "w", "s", "w", "e", "n", "w", "s", "w", "e", "n", "w", "s", "w", "e", "n", "w", "s", "w", "e"])
print(type(policy))
print(policy.shape)

# The following np.array 'v' has the correct format (but is just a random
# collection of floats).
v = np.random.rand(25)
print(v)

# Please write your code for Exercise 1 here. We will mark your coursework by checking
# the values of the variables policy and v in this cell. Your code should compute the
# values of policy and v from scratch when this cell is executed, using the value
# iteration algorithm.
