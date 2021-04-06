# 구현
# 문자열 재정렬
# 데이터 받음
data = input()
# 알파벳만 따로 담을 배열
result = []
value = 0
# 데이터를 돌면서 알파벳과 숫자 구분
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()
if value != 0:
    result.append(str(value))

# 리스트를 문자열로 변경해서 출력
print(''.join(result))


