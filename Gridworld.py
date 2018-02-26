import numpy as np
import random
#% matplotlib inline


class Gridworld:
    '''

    '''

    def __init__(self):
        self.num_rows = 5
        self.num_cols = 5
        self.num_cells = self.num_cols * self.num_rows

        # Choose starting position of the agent randomly among the first 5 cells
        self.agent_position = np.random.randint(0, 5)

        # Choose position of the gold and bomb
        self.bomb_positions = np.array([18])
        self.gold_positions = np.array([23])
        self.terminal_states = np.array([self.bomb_positions, self.gold_positions])

        # Specify rewards
        self.rewards = np.zeros(self.num_cells)
        self.rewards[self.bomb_positions] = -10
        self.rewards[self.gold_positions] = 10

        # Specify available actions
        self.actions = ["UP", "RIGHT", "DOWN", "LEFT"]

    def get_available_actions(self):
        return self.actions

    def make_step(self, action):

        if random.random() < 0.2:
            i = np.random.randint(0, 4)
            action = self.actions[i]

        old_position = self.agent_position
        new_position = self.agent_position

        # Update new_position based on the chosen action and check whether agent hits a wall.
        if action == "UP":
            candidate_position = self.agent_position + self.num_cols
            if candidate_position < self.num_cells:
                new_position = candidate_position
        elif action == "RIGHT":
            candidate_position = self.agent_position + 1
            if candidate_position % self.num_cols > 0:
                new_position = candidate_position
        elif action == "DOWN":
            candidate_position = self.agent_position - self.num_cols
            if candidate_position >= 0:
                new_position = candidate_position
        elif action == "LEFT":
            candidate_position = self.agent_position - 1
            if candidate_position % self.num_cols < self.num_cols - 1:
                new_position = candidate_position
        else:
            raise ValueError('Action was mis-specified!')

        # Update the position of the agent.
        self.agent_position = new_position

        # Get reward
        reward = self.rewards[new_position]

        # Deduct 1 from reward if agent moved
        # if old_position != new_position:
        # reward -= 1

        # Deduct 1 from reward for every attempted move
        reward -= 1

        return reward

    def is_terminal(self, state):
        if state in self.terminal_states:
            return True
        else:
            return False

    def choose_random_action(self, available_actions):
        number_of_actions = len(available_actions)
        random_index = np.random.randint(0, number_of_actions)
        action = available_actions[random_index]
        return action

    def get_bomb_location(self):
        return self.bomb_positions

    def get_gold_location(self):
        return self.gold_positions
