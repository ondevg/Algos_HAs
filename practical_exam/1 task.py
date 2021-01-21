# def part_sum(n, a):
#     i = 0
#     s = 0
#     while i <= n:
#         s += i * a**i
#         i += 1
#     else:
#         return s
#     return part_sum(n, a)
#
#
# n, a = map(int, input().split())
# print(part_sum(n, a))
n, a = map(int, input().split())
print(int((n * a ** (n + 2) - (n + 1) * a ** (n + 1) + a) / (1 - a) ** 2))

n, a = map(int, input().split())


def part_sum(n, a):
    if a != 1:
        return int((n * a**(n+2) - (n + 1) * a**(n+1) + a)/(1 - a)**2)
    else:
        return sum(i for i in range(0, n + 1))
