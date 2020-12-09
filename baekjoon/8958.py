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


def qs(array):
    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp
    return array




