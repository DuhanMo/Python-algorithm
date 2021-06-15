def solution(n):
    answer = 0
    f0 = 0
    f1 = 1
    for x in range(1,n):
        answer = f0 + f1
        f0 = f1
        f1 = answer

    return answer


print(solution(123))
