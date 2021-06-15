n = int(input())
user_list = list(map(int, input().split()))
a, b = map(int, input().split())


answer = 0
for i in range(a-1, b):
    answer += user_list[i]

print(answer)