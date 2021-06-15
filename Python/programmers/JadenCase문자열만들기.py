def solution(s):
    last_space = False
    if s[-1] == ' ':
        last_space = True
    print(last_space)
    answer = ''
    s = s.split(' ')
    for x in s:
        answer += x.capitalize() + ' '

    answer = answer.strip()
    if last_space:
        return answer + ' '
    else:
        return answer


s = "for the last week "
print(solution(s))
