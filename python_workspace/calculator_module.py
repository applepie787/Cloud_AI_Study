
# 사칙연산 모듈
def add_(value_1, value_2):
    return value_1 + value_2

def subtract_(value_1, value_2):
    return value_1 - value_2

def multiply_(value_1, value_2):
    return value_1 * value_2

def divide_(value_1, value_2):
    return value_1 / value_2



print("Calculator_module ", __name__)

# 실행되는 파이썬 파일이 __main__이 된다.
if __name__ == "__main__":
    # 테스트를 위한 코드를 이러한 형태로 구현할 수 있다.
    print("calculator_moldule 엔트리포인트")
