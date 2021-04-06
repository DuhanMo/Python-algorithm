# 재귀함수 유클리드 호제법(최대공약수) 계산
# GCD ( 최대 공약수 Greatest Common Divider)
# 유클리드 호제법
# A와 B 가 있을 때 A를 B로 나눈 나머지를 R이라고 했을 때 A와 B의 최대공약수와
# B와 R의 최대공약수가 같음

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


print('최대공약수', gcd(21, 3))
print('최소공배수', lcm(21, 3))
