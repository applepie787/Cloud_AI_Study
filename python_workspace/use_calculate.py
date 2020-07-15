import calculator_module

# 실행하는 .py파일이 엔트리포인트.
# 즉, 엔트리포인트가 되는 모듈(.py)의 이름이 곧 "__main__"이 된다.
print("20 + 10 =", calculator_module.add_(20, 10))
print("20 - 10 =", calculator_module.subtract_(20, 10))
print("20 * 10 =", calculator_module.multiply_(20, 10))
print("20 / 10 =", calculator_module.divide_(20, 10))

print("use_calculator.py ", __name__)
if __name__ == "__main__":
    print("use_calculator.py 엔트리포인트")