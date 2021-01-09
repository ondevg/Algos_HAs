import random

def selection_sort(x):
    N = len(x)
    #lst = []
    for i in range (N-1):
        i_min = i
        for j in range (i+1, N):
            if x[j] < x[i_min]:
                i_min = j
        x[i], x[i_min] = x[i_min], x[i]


arr = random.sample(range(0, 50), 50)
print(arr)
print(selection_sort(arr))

