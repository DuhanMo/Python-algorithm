def is_perfect(n):
    aliquot = []
    for i in range(1, n):  # n바로 직전의 수까지만 돌아서 n 은 약수리스트에 들어가지 않는다
        if n % i == 0:
            aliquot.append(i)

    if sum(aliquot) == n:
        return True
    else:
        return False


a, b = map(int, input().split())

for i in range(a,b+1):
    if is_perfect(i):
        print(i,end=' ')
