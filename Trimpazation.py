def fast_trimp(n, m, q0):
    c = [0] * m
    m_div2 = m // 2
    min_val = - m_div2
    q = q0
    for i in range(N):
        x = q % M - m_div2
        c[x - min_val] += 1
        q = ((q * quantum_a) % quantum_m)
    res = 0
    k = 1
    for i in range(M):
        res += (i + min_val) * ((k + (k + c[i] - 1)) * c[i]) // 2
        k += c[i]
    return res


from time import time

# set the following flag to True to estimate execution time
#
# Exact execution time on you device may be different
# from one on Yandex contest platform!
#
# The flag MUST be False when you are submitting your solution!
estimate_execution_time = True

# Fixed parameters of quantum process:
quantum_a = 7**5
quantum_m = 2**31 - 1


def analyze_trimpazation(n, m, q0):
    '''
    This function generates data with given parameters
    and calculates desired Y value.
    You need to modify it to make it execute faster.
    You can check your progress using estimate_execution_time flag
    at the top of the file.
    '''
    m_div2 = m // 2
    q = q0

    # generating x data:
    x = []
    for i in range(n):
        x_i = q % m - m_div2
        x.append(x_i)
        q = ((q * quantum_a) % quantum_m)

    # sorting x data:
    x.sort()

    # calculating sum:
    res = 0
    for i, v in enumerate(x):
        res += (i + 1) * v

    return res


# if __name__ == '__main__':
N, M, q0 = map(int, input().split())
t = time()
print(analyze_trimpazation(N, M, q0))
if estimate_execution_time:
    print(f'Execution time = {time() - t:.8f} seconds')