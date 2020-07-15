"""
print('hello world')
for i in range(1, 10):
    for j in range(0, i):
        print('*', end='')
    print('')

#print('test_1 is over')

for i in range(1, 10):
    for j in range(i, 10):
        print('*', end='')
    print('')
"""
print("hello \'python\'") # 특수문자 사용지 역슬래쉬로 사용하는게 일반적인 방법

i = 10

print("hello \'python\'", i, "star" and "test_1")


name = "홍길동"
age = 30
print("이름은 " + name + " 나이는 " + str(age) + " 입니다.")
print("이름은 {0}이고 나이는 {1} 입니다" .format(name, age)) # 이러한 대입연산 형태의 format 메서드를 사용하기도 한다

