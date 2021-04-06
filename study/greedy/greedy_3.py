# 주어진 숫자 문자열 S를 이용해 가장 큰 수를 만들어라

data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result == 0:
        result += num
    else:
        result *= num

print(result)
