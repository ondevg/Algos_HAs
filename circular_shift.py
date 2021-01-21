def prefix_func(s):
    d = [0] * (len(s) + 1)
    for i in range(2, len(d)):
        d[i] = d[i - 1]
        while s[i - 1] != s[d[i]] and d[i] > 0:
            d[i] = d[d[i]]
        if s[i - 1] == s[d[i]]:
            d[i] += 1
    return d


def find_substr(s, p):
    substr = []
    d = prefix_func(p + '$' + s)
    for i in range(len(p) + 1, len(d)):
        if d[i] == len(p):
            substr.append(i - 2 * len(p) - 1)
    return substr


s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print(-1)
else:
    s22 = s2 + s2
    res = find_substr(s22, s1)
    if len(res) == 0:
        print(-1)
    else:
        print(res[0])