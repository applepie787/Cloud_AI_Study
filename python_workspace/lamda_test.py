def increase_(value):
    return value + 10

def decrease_(value):
    return value - 5

# def call_change_data(func_, original_list_):
#     new_list = []
#     for index_, value_ in enumerate(original_list_):
#         new_list.append(func_(value_))
    
#     return new_list



original_list = [10, 20, 30, 40, 50]
print("Before : {0}".format(original_list))

# 아래와 같이, map 함수 내에서 func 부분을 lambda식으로 구현하여 사용 할 수 있다.
print("new-list : {0}".format(list(map(lambda value : value + 10, original_list))))
print("new-list : {0}".format(list(map(lambda value : value - 5, original_list))))
print("new-list : {0}".format(list(filter(lambda value : value < 30, original_list))))
# new_list = map(increase_, original_list)
# print(new_list)

# call_change_data(increase_, 10)
# print("After : {0}".format(original_list))  
# call_change_data(decrease_, 5)
# print("After : {0}".format(original_list))

# print("new-list : {0}".format(call_change_data(increase_, original_list)))
# print("new-list : {0}".format(call_change_data(decrease_, original_list)))
print("original list : {0}".format(original_list))