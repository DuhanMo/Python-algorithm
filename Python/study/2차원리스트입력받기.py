n, m = map(int, input().split())

myList = [0 for _ in range(n)]

for i in range(n):
    myList[i] = list(map(int, input().split()))

print(myList)