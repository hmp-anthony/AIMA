
L = [{2: ['suck', {8: [], 4: 'loop'}], 4: 'loop'}]
L = L[0]

print(L)

keys = list(L.keys())
print(keys)


for k in keys:
    if(type(L[k]) == list):
        print(L[k])
