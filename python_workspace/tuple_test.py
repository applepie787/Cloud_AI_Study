# 튜플 - 리스트와 유사한 자료형
# 한번 결정된 요소는 바뀔 수 없습니다.

tuple_data = (10, 20, 30)
tuple_data2 = 10, 20, 30 # 괄호가 없어도 튜플로 선언됩니다.

print(tuple_data)
print(tuple_data2)
print(type(tuple_data))
print(type(tuple_data2))

# tuple_data[0] = 100 튜플에 새로운 값을 할당 할 수는 없다.

name, age, major = "이루다", 28, "전자전기공학"
print(name,"|", age,"|", major)

# swapping
a, b = 10, 20
print(a, b)
temp = a
a = b
b = temp
print(a, b)

# 튜플을 사용하면 한줄로 스왑 할 수 있다.
a, b = b, a
print(a, b)