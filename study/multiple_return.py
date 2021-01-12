# 패킹
def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var


# 언팩킹
a, b, c, d = operator(7, 3)
print(a, b, c, d)

# 람다 표현식 예시: 내장 함수에서 자주 사용되는 람다 함수

array = [('홍길동', 50), ('이순신', 30), ('아무개', 22)]

print(sorted(array, key=lambda x: x[1]))


# 람다표현식 예씨 : 여러개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda one, two: one + two, list1, list2)
print(list(result))

