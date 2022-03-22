import random as r
import ShortCutEnvironment as env
class QLearningAgent(object):

    def __init__(self, n_actions, n_states, epsilon, alpha, gamma):
        # self.n_actions  = n_actions
        # self.n_states   = n_states                                          
        self.alpha      = alpha                                             # learning rate
        self.gamma      = gamma                                             # discount factor
        self.epsilon    = epsilon                                           # chance of exploration                                         
        self.Q = [[0 for _ in range(n_actions)] for _ in range(n_states)]   # mean rewards
        self.n = [0 for _ in range(n_actions)]                              # number of times an action has been taken
        pass
        
    def select_action(self, state):
        if (0.001 * r.randint(1, 1000) <= 1 - self.epsilon):                # generate random number between 0.00 and 1.00.
            a = self.Q[state].index(max(self.Q[state]))                     # if random number is bigger than 1-epsilon, return the index of the highest mean
        else:
            copy = self.Q[state].copy()                                     # create a copy of Q so  the value is not deleted from the actual list
            copy.remove(max(self.Q[state]))                                 # delete the highest value from the list
            random_action = r.choice(copy)                                  # choose a random action from the remaining actions
            a = self.Q[state].index(random_action)                          # return the index of chosen action
        return a
        
    def update(self, state, action, reward):
        target = self.gamma * max(self.Q[self.select_action(state)])                        # find the next state after action is taken
        self.n[action] += 1
        self.Q[state][action] += (self.alpha *  (reward + target + self.Q[state][action]))  # update the means according to Q-learning rule
        pass

class SARSAAgent(object):

    def __init__(self, n_actions, n_states, epsilon):
        # self.n_actions = n_actions
        # self.n_states = n_states
        self.epsilon = epsilon
        self.Q = [[0 for _ in range(n_actions)] for _ in range(n_states)]   # mean rewards
        self.n = [0 for _ in range(n_actions)]                              # number of times an action has been taken
        pass
        
    def select_action(self, state):
        # TO DO: Add own code
        if (0.001 * r.randint(1, 1000) <= 1 - self.epsilon):                # generate random number between 0.00 and 1.00.
            a = self.Q[state].index(max(self.Q[state]))                     # if random number is bigger than 1-epsilon, return the index of the highest mean
        else:
            copy = self.Q[state].copy()                                     # create a copy of Q so  the value is not deleted from the actual list
            copy.remove(max(self.Q[state]))                                 # delete the highest value from the list
            random_action = r.choice(copy)                                  # choose a random action from the remaining actions
            a = self.Q[state].index(random_action)                          # return the index of chosen action
        return a

    def e_greedy(self, actions):
        '''This function is not needed at all, as select_action is
           e-greedy but I was too tired to think about how to
           implement that in the update here with indexes :`)'''
        if (0.001 * r.randint(1, 1000) <= 1 - self.epsilon):          # generate random number between 0.00 and 1.00.
            a = max(actions)                                          # if random number is bigger than 1-epsilon, return the index of the highest mean
        else:
            copy = actions.copy()                                     # create a copy of Q so  the value is not deleted from the actual list
            copy.remove(max(actions))                                 # delete the highest value from the list
            random_action = r.choice(copy)                            # choose a random action from the remaining actions
            a = actions[random_action]                                # return the index of chosen action
        return a
        
    def update(self, state, action, reward):
        target = self.gamma * self.e_greedy(self.Q[self.select_action(state)])              # find the next state after action is taken
        self.n[action] += 1
        self.Q[state][action] += (self.alpha *  (reward + target + self.Q[state][action]))  # update the means according to Q-learning rule
        pass

class ExpectedSARSAAgent(object):

    def __init__(self, n_actions, n_states, epsilon):
        self.n_actions = n_actions
        self.n_states = n_states
        self.epsilon = epsilon
        # TO DO: Add own code
        pass
        
    def select_action(self, state):
        # TO DO: Add own code
        a = r.choice(range(self.n_actions)) # Replace this with correct action selection
        return a
        
    def update(self, state, action, reward):
        # TO DO: Add own code
        pass