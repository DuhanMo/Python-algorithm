# 구현
# 나이트가 움직일 수 있는 경우의 수


input_data = input()
row = int(input_data[1])  # y
column = int(ord(input_data[0])) - int(ord('a')) + 1  # x
count = 0
steps = [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
for step in steps:
    next_row = row + step[1]
    next_column = column + step[0]

    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        count += 1

print(count)
