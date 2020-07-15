import datetime
now_ = str(datetime.datetime.now()).split()
date_ = now_[0]
month_ = (date_.split('-'))[1]

# 아래와 같은 방법으로 '달' 값을 바로 뽑아 낼 수 있다. 위와 같은 방법으로 parshing 하지 않아도 ok
month_2 = datetime.datetime.now().month
print(month_2)

# month_ = input("달을 입력하세요 : ")
print("현재는", month_, "월달 입니다")

date_nums = 0
if(month_ == '02'):
    date_nums = 29
elif(month_ == '04' or month_ == '06' or month_ == '09' or month_ == '12'):
    date_nums = 30
else:
    date_nums = 31

print("이번달은", date_nums,"만큼 일수가 있습니다.")