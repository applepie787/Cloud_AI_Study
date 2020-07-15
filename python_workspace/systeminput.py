# hello = input("인사말 입력 : ") # 키보드로 입력받는 값은 기본은 str 타입이다.
# print(type(hello), hello)

# num = input("add number : ")
# print(int(num) + 100 ) # num : 숫자문자 아닌 문자인경우 ValueError

a = 2
b = 10.424

print(a + b)
print(a * b)
print(b % a)
print(b // a, " ", b / a) # // 연산은 나눗셈 후 소숫점 값을 버림.

num1 = float(input("첫번쨰 데이터를 입력하세요"))
num2 = float(input("두번쨰 데이터를 입력하세요"))

print("입력하신 데이터 {0} + {1} = {2} 입니다" .format(num1, num2, num1 + num2))
print("입력하신 데이터 {0} - {1} = {2} 입니다" .format(num1, num2, num1 - num2))
print("입력하신 데이터 {0} * {1} = {2} 입니다" .format(num1, num2, num1 * num2))
print("입력하신 데이터 {0} / {1} = {2} 입니다" .format(num1, num2, num1 / num2))
print("입력하신 데이터 {0} % {1} = {2} 입니다" .format(num1, num2, num1 % num2))
print("입력하신 데이터 {0} // {1} = {2} 입니다" .format(num1, num2, num1 // num2))