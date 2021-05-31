def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)


def solution(arr):
    answer = 0
    l = lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        l = lcm(l, arr[i])

    return l

import math

def solution2(arr):
    answer = 0
    l = math.lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        l = math.lcm(l, arr[i])

    return math.lcm(*arr)


arr = [2,6,8,14]
print(solution2(arr))