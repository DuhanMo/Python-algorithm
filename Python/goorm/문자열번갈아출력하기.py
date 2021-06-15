first = input()
n = len(first)
lt = 0
rt = n - 1
mid_index = (n - 1) // 2
answer = ''

for i in range(mid_index + 1):
    answer += first[lt]
    answer += first[rt]
    lt += 1
    rt -= 1

if (n % 2 == 1):
    answer = answer[:-1]

print(answer)
