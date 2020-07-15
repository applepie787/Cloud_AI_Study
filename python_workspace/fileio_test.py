# test data file 출력
write_file = open("hello.txt", "w")
write_file.write("Hello Python....")
write_file.close()

# file 입력 -> console 출력
write_file = open("hello.txt", "r")
print("입력 데이터 : ", write_file.read())
write_file.close()

# console 입력 -> file 출력
input_ = input("데이터를 입력해 주세요 : ")
write_file = open("hello.txt", "a")
write_file.write("\n" + input_)
write_file.close()

# file입력 -> file 출력
read_file = open("hello.txt", "r")
write_file = open("copy_hello.txt", "w")
write_file.write(read_file.read())
read_file.close()   # 파일 입출력 이후, 꼭 close() 해준다.
write_file.close()
