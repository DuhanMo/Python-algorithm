# 구현
# N시 59분 59초까지 3이 포함된 모든 수를 셈

h = int(input())
count = 0
for i in range(1, h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1


print(count)

