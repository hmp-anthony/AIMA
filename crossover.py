import random 

def cycle_crossover(A, B):
    data = [A, B]
    n = len(A)
    child = [None] * n
    c = random.choice([0,1])
    # the first cycle
    child[0] = data[c][0]
    cycle = [data[c][0]]
    n = data[1-c].index(data[c][0])
    child[n] = data[c][n]
    cycle.append(data[c][n])

    while(cycle[-1] != cycle[0]):
        n = data[1-c].index(cycle[-1])
        child[n] = data[c][n]
        cycle.append(data[c][n])

    while(None in child):
        i = child.index(None)
        child[i] = data[1-c][i]
        cycle = [data[1-c][i]]
        n = data[c].index(data[1-c][i])
        child[n] = data[1-c][n]
        cycle.append(data[1-c][n])
        while(cycle[-1] != cycle[0]):
            n = data[c].index(cycle[-1])
            child[n] = data[1-c][n]
            cycle.append(data[1-c][n])
        c = 1-c
    
    return child


A = ['A', 'B', 'C', 'T', 'D', 'E', 'F', 'G', 'Z', 'R', 'Y', 'Q', 'M', 'N']
B = ['R', 'A', 'M', 'N', 'D', 'G', 'B', 'F', 'E', 'C', 'T', 'Y', 'Z', 'Q']

#A = [1,2,3,4,5,6,7,8,9,10]
#B = [5,6,7,8,9,10,1,2,3,4]

print(cycle_crossover(A, B))


