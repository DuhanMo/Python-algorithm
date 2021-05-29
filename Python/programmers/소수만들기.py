from itertools import combinations

def isPrime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
    return True


def solution(nums):
    combi_array = list(combinations(nums, 3))
    count = 0
    for combi in combi_array:
        if isPrime(sum(combi)):
            count += 1
    return count


nums = [1,2,7,6,4]

print(solution(nums))
