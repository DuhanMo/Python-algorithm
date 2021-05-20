def solution(n):
    answer = ''
    list = ['4','1','2']
    while n > 0:
        nam = n % 3
        n = n // 3
        if nam == 0:
            n -= 1
        answer = list[nam] + answer

    return answer


print(solution(15))