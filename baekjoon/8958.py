n = int(input())

for i in range(n):
    score = 0
    sum_score = 0
    quiz = input()
    for j in quiz:
        if j == "O":
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)

