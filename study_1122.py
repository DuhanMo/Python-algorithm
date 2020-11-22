# print("나는 {age}살이며 {color}색을 좋아합니다.".format(age=20,color="빨강"))

print("나는 {1}살 이며 {0}색을 좋아합니다.".format(20,"빨강"))


age = 20
color = "빨강"
# print(f"나는 {age}살이며 {color}색을 좋아합니다.")

# # 리스트
# subway999 = ["유재석","조세호","박명수"]
# # 조세호씨 몇번칸에 타고있나?
# print(subway999.index("조세호"))

# # 하하씨가 다음칸에 탐
# subway999.append("하하")
# print(subway999)

# # 정형돈씨를 유재석 조세호 사이에 탄다
# subway999.insert(1,"정형돈")
# print(subway999)

# # 지하철에 있는 사람을 뒤에서부터 뺌
# print(subway999.pop())
# print(subway999) 
# print(subway.pop())
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway) 

# # 유재석을 한번 더 넣음
# subway999.append("유재석")
# print(subway999.count("유재석"))

# num_list = [5,3,7,1,9]
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

# # 사전
# cabinet = {3:"유재석",100:"김태호"}
# print(cabinet[3])
# print(cabinet.get(3))
# print(cabinet.get(5))
# print(cabinet.get(5,"사용 가능"))
# print("hi")

# print(3 in cabinet)
# print(5 in cabinet)

cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국"
print(cabinet)

# del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.clear())