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

def partially_mapped_crossover(A, B):
    n = len(A)
    left = random.randint(0, n)
    right = random.randint(0, n)
    if left > right:
        left, right = right, left
    AS = A[left : right]
    BS = B[left : right]
    A[left : right] = BS
    B[left : right] = AS

    # create mapping
    map_1 = {}
    map_2 = {}
    for i in range(left, right):
        map_1[A[i]] = B[i]
        map_2[B[i]] = A[i]

    # map duplicates
    R = list(range(left)) + list(range(right, n))
    for i in R:
        while A[i] in BS:
            A[i] = map_1[A[i]]
        while B[i] in AS:
            B[i] = map_2[B[i]]
    return random.choice([A,B])
     


A = ['A', 'B', 'C', 'T', 'D', 'E', 'F', 'G', 'Z', 'R', 'Y', 'Q', 'M', 'N']
B = ['R', 'A', 'M', 'N', 'D', 'G', 'B', 'F', 'E', 'C', 'T', 'Y', 'Z', 'Q']

#A = [1,2,3,4,5,6,7,8,9,10]
#B = [5,6,7,8,9,10,1,2,3,4]

#A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#B = [2, 4, 6, 8, 7, 5, 3, 1]
#B = [3, 7, 5, 1, 6, 8, 2, 4, 9]

print(A)
print(B)
print("algorithm output ===")
print("cycle crossover")
print(cycle_crossover(A, B))
print("partially mapped")
print(partially_mapped_crossover(A, B))


