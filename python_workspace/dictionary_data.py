
# 딕셔너리(맵) 타입은 {}으로 데이터를 묶고, 키(key) 값을 왼쪽에, 오른쪽에 값(value)를 위치 시킨다.
# 딕셔너리 타입은 머신러닝 뿐만이 아니라, Json 파일을 다루는 경우에도 자주 쓰임.

AI_1 = {
    "name" : "이루다",
    "age" : 28,
    "major" : "전자전기공학부"
}
AI_2 = {
    "name" : "홍길동",
    "age" : 25,
    "major" : "컴퓨터공학"
}
AI_3 = {
    "name" : "123",
    "age" : 5456,
    "major" : "5487"
}

# 딕셔너리를 list 타입 데이터에 넣을 수도 있음
AI_s = [AI_1, AI_2, AI_3]

for i in AI_s:
    print(i)
    if(i["name"] == "이루다" ):
        print(i["age"])

for ai in AI_s:
    print("이름 : {0} , 나이 : {1} , 전공 : {2}".format(ai["name"], ai["age"], ai["major"]))


# 딕셔너리의 key값에 매칭되는 vlaue는 언제든지 대입으로 변경할 수 있다.
AI_1["major"] = "컴퓨터공학"

for ai in AI_s:
    print("이름 : {0} , 나이 : {1} , 전공 : {2}".format(ai["name"], ai["age"], ai["major"]))

# del : 요소제거
for ai in AI_s:
    del ai["age"]
    print(ai)

print("______________________________________________")

# enumerate()
print("enumerate 함수 적용")
for i, value in enumerate(AI_s):
    print("{0}번째 : {1}".format(i, value))
print("______________________________________________")


print("AI_1 dictionary 정보 : iten() 사용")
print(AI_1.items())
print("______________________________________________")

print("list comprehension 기능")
array_ = ["123", "456", "678", "987"]
new_array_ = [i for i in array_ if array_ != "123"]
print(new_array_)