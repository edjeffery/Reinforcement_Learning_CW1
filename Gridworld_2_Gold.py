import numpy as np


class Gridworld:
    ''' Defines the properties and functionality of the Gridworld

    Attributes:
        num_rows (int): Number of rows
        num_cols (int): Number of columns
        num_dimensions (int): Number of variations of gridworld that can occur (i.e. 2 gold, 1st taken & 2nd remaining or 1st remaining and 2nd left)
        num_cells (int): Number of cells in Gridworld
        num_states (int): Number of possible states in Gridworld (dimension factor of num_cells)
        bomb_positions (np.array): State locations of bombs
        gold_positions (np.array): State locations of gold
        terminal_gold_positions (np.array): State locations of gold pieces that are also terminal states
        terminal_states (np.array): State locations of terminal states
        rewards (np.array): Reward from being in a given state
        actions (list): Available actions from any given state

    '''

    def __init__(self):
        """Sets up Gridworld"""
        self.num_rows = 5
        self.num_cols = 5
        self.num_dimensions = 3
        self.num_cells = self.num_cols * self.num_rows                          #25
        self.num_states = self.num_cols * self.num_rows * self.num_dimensions   #75

        # Choose positions of the gold and bomb in each dimension
        self.bomb_positions = np.array([18, 43, 68])
        self.gold_positions = np.array([12, 23, 37, 73])
        self.terminal_gold_positions = np.array([37, 73])
        self.terminal_states = np.concatenate([self.bomb_positions, self.terminal_gold_positions])

        # Specify rewards
        self.rewards = np.zeros(self.num_states)
        self.rewards[self.bomb_positions] = -10
        self.rewards[self.gold_positions] = 10

        # Specify available actions
        self.actions = ["n", "e", "s", "w"]

    def get_available_actions(self):
        """ Returns available actions in any given state """
        return self.actions

    def make_step(self, current_state, action):
        """ Computes the new state and reward for being in that new state """

        if current_state == 12:
            current_state = current_state + 50
        elif current_state == 23:
            current_state = current_state + 25

        new_state = current_state

        if 0 <= current_state < 25:
            dimension = 1
        elif 25 <= current_state < 50:
            dimension = 2
        elif 50 <= current_state < 75:
            dimension = 3
        else:
            print("Error in dimension")

        # Update new_position based on the chosen action and check whether agent hits a wall.
        if action == "n":
            temp_state = current_state + self.num_cols
            if temp_state < self.num_cells * dimension:
                new_state = temp_state
        elif action == "e":
            temp_state = current_state + 1
            if temp_state % self.num_cols > 0:
                new_state = temp_state
        elif action == "s":
            temp_state = current_state - self.num_cols
            if temp_state >= 0 + (25 * (dimension - 1)):
                new_state = temp_state
        elif action == "w":
            temp_state = current_state - 1
            if temp_state % self.num_cols < self.num_cols - 1:
                new_state = temp_state
        else:
            raise ValueError('Action was mis-specified!')

        # Get reward
        reward = self.rewards[new_state]

        # Deduct 1 from reward for every attempted move
        reward -= 1

        return (new_state, reward)

    def is_terminal(self, state):
        """Checks if a state is terminal or not"""
        if state in self.terminal_states:
            return True
        else:
            return False
