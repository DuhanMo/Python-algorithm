def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append("")
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]



participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))