
# 함수의 def 함수명(argument_list) 
#   구현 
#   return return data

def print_n_time(value, n):
    for i in range(n):
        print(value)

# 가변 매개변수 사용하려면, 반드시 와야하는 매개변수는 앞쪽으로 받는다.
def print_n_time_2(n = 2, *value):
    for i in range(n):
        print(value)

def print_n_time_3(*value, n = 2):
    for i in range(n):
        print(value, end="\t")

    print()
    # return - 함수 종료 
    # return data - 호출한 족에 데이터 전달
    # return data, data - 하나의 객체(tuple)로 전달
    return "print success", "success" 



# 함수사용
# 함수명(argument_list)

print_n_time("function", 3)
print_n_time(3, 3)

# 가변 매개변수 사용 시 argument_list는 0 ~ n 개
# 기본값에 명시된 변수명 = 사용자정의값
print_n_time_2(3)
print_n_time_2(3, "가변매개변수", 3)
print_n_time_2(3, "가변매개변수", 3, "가변매개")

print(print_n_time_3(3, n = 3))
messege_ = print_n_time_3(3, "가변", "가변매개")
print(messege_)