array_list = [123, 424, 12, "홍길동", 242.23, False, True, "홍길동"]
print(array_list)

# for i in range(0, len(array_list)):
#     print("data type of array_list[" + str(i) + "] = ", type(array_list[i]))

for i in array_list:
    print(type(i))

# 기존에 int를 가르키는 위치에 다른 type의 값을 넣어도 해당 list가 그 변수를 '가르키도록' 수정되는 것.
array_list[0] = 124.42415
print(array_list[0], type(array_list[0]))
print("_________________________________________")
print("")

list_array = [[1,2,3], [4,5,6],[7,8,9], "asd"]
print(list_array)
print(type(list_array))
print(type(list_array[0]), len(list_array[0]))
print(type(list_array[0][1]))
print(type(list_array[3]),len(list_array[3]))
print(len(list_array))
print("_________________________________________")
print("")


