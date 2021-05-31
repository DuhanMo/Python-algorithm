def solution(s):
    answer = ' '
    s = s.split(' ')
    for x in s:
        answer += x.capitalize() + ' '

    return answer.strip()

s = "for the last week"
print(solution(s))