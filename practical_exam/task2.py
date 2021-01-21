def calc(mins):
    s = 0
    i = 0
    while s < mins:
        s += time_each[i]

        if s <= mins:
            i += 1
        else:
            return i
    return i


n, m = map(int, input().split())
time_each = sorted(list(map(int, input().split())))
print(calc(m))