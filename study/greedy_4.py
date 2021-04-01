# 공포도 측정해서 그룹짓기 공포도가 x인 사람은 그룹에 총 x명 이상으로 구성되어야한다

n = int(input())
array = list(map(int, input().split()))
array.sort()
result = 0
count = 0
for i in array:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)