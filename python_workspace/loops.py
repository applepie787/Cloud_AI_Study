array_ = [1, 2, 3, 4, 5]

for data in array_:
    print(data, end="") # print로 인한 라인 변경을 막아준다.


print("")
for data in array_:
    print(data)
print("_______________________________________________")


for i in range(len(array_)):
    print(array_[i])
print("_______________________________________________")


for i in reversed(range(len(array_))):
    print(array_[i])
print("_______________________________________________")

list_ = range(1, 11)
i = -1
while(True):
    if(i >= len(list_)):
        break
    i += 1
    if( i % 2 == 0):
        continue
    print(list_[i])
print("_______________________________________________")


for x in range(2,10):
    for y in range(1, 10):
        print( x, " * ", y, " = ", x*y)
    print("_______________")

for y in range(1,10):
    for x in range(2, 10):
        print("{0} * {1} = {2}".format(x, y, x*y), end="\t")
    print("")

print("_______________________________________________")

