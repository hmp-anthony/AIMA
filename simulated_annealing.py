# remember that search_2 file is a file that I generated that 
# uses the data structures that work with the 4th edition code.
# you will need to visit my github repo https://github.com/hmp-anthony
# to access it.
from search_2 import *
from utils import *
import numpy as np
import matplotlib.pyplot as plt

romania = {'A': ( 76, 497), 'B': (400, 327), 'C': (246, 285), 'D': (160, 296), 'E': (558, 294), 
           'F': (285, 460), 'G': (368, 257), 'H': (548, 355), 'I': (488, 535), 'L': (162, 379),
           'M': (160, 343), 'N': (407, 561), 'O': (117, 580), 'P': (311, 372), 'R': (227, 412),
           'S': (187, 463), 'T': ( 83, 414), 'U': (471, 363), 'V': (535, 473), 'Z': (92, 539)}

distances = {}
cities = []

for city in romania.keys():
    distances[city] = {}
    cities.append(city)

for name_1, coordinates_1 in romania.items():
        for name_2, coordinates_2 in romania.items():
            distances[name_1][name_2] = np.linalg.norm(
                [coordinates_1[0] - coordinates_2[0], coordinates_1[1] - coordinates_2[1]])
            distances[name_2][name_1] = np.linalg.norm(
                [coordinates_1[0] - coordinates_2[0], coordinates_1[1] - coordinates_2[1]])

def cost(route):
    c = 0
    for i in range(len(route)-1):
        c += distances[route[i]][route[i+1]]
    c += distances[route[0]][route[-1]]
    return c

class TSP(Problem):
    
    def two_opt(self, state):
        neighbour_state = state[:]
        left = random.randint(0, len(neighbour_state) - 1)
        right = random.randint(0, len(neighbour_state) - 1)
        if left > right:
            left, right = right, left
        neighbour_list = list(neighbour_state)
        x = neighbour_list[left: right + 1]
        neighbour_list[left: right + 1] = x[::-1]
        neighbour_state = tuple(neighbour_list)
        return neighbour_state
        
    def is_goal(self, state):
        return cost(state) < 1603
    
    def actions(self, state): 
        """The places neighboring `state`."""
        new_states = list()
        new_states.append(state)
        for i in range(10):
            new_state = self.two_opt(state)
            new_states.append(new_state)
        return new_states
    
    def result(self, state, action):
        """Go to the `action` place, if the map says that is possible."""
        return action
    
    def action_cost(self, s, action, s1):
        """The distance (cost) to go from s to s1."""
        if(type(s1) == tuple):
            return cost(s1)
        if(type(s1) == list):
            return cost(tuple(s1))
       

    def value(self, state):
        """ value of path cost given negative for the given state """
        return -1 * self.action_cost(None, None, state)


def exp_schedule(k=20, lam=0.15, limit=1000):
    """One possible schedule function for simulated annealing"""
    return lambda t: (k * math.exp(-lam * t) if t < limit else 0)


def simulated_annealing(problem, schedule=exp_schedule()):
    """[Figure 4.5] CAUTION: This differs from the pseudocode as it
    returns a state instead of a Node."""
    current = Node(problem.initial)
    for t in range(sys.maxsize):
        T = schedule(t)
        if T == 0:
            return current.state
        neighbors = expand_and_return_node_list(problem, current)
        if not neighbors:
            return current.state
        next_choice = random.choice(neighbors)
        delta_e = problem.value(next_choice.state) - problem.value(current.state)
        if delta_e > 0 or probability(math.exp(delta_e / T)):
            current = next_choice


tsp = TSP(cities)
path = simulated_annealing(tsp)

data = []
for p in path:
    data.append(romania[p])
data.append(data[0])

x_val = [x[0] for x in data]
y_val = [x[1] for x in data]

plt.plot(x_val,y_val)
plt.plot(x_val,y_val,'or')
plt.show()
