# 메뉴를 선택하고, 수강생 정보는 Dict 타입으로 받은 뒤, list로 저장한다.


ai_list = []

# def register_(al_dictionary): name, age, major 정보의 dictionary
#            return 성공여부 message
# def al_list() : return diction 정보가 저장된 list
# def ai_remove(name) : 매개변수 탈퇴할 name 정보
#            return 성공여부 message
# def ai_update(ai_dictionary) : 수정할 name, age, major 정보의 dict
#            return 성공여부 message
# def ai_search(name) : 매개변수 검색할 name
#            return 검색한 neme의 index

def register_(al_dictionary):
    ai_list.append(al_dictionary)
    return "<수강생이 성공적으로 등록되었습니다.>"

def ai_list_():
    for i in range(len(ai_list)):
            print("{0} -- 이름 : {1}, 나이 : {2}, 전공 : {3}".format(i + 1, ai_list[i]["name"], ai_list[i]["age"], ai_list[i]["major"]))

def ai_remove_(name_):
    for i, dict_ in enumerate(ai_list):
        if(dict_["name"] == name_):
            del ai_list[i]
    return "<수강생이 성공적으로 삭제되었습니다.>"

def ai_update_(ai_dictionary):
    for dict_ in ai_list:
        if(dict_["name"] == ai_dictionary["name"]):
            dict_["age"] = ai_dictionary["age"]
            dict_["major"] = ai_dictionary["major"]
    return "<수강생이 성공적으로 수정되었습니다.>"

def ai_search(name_):
    for i, dict_ in enumerate(ai_list):
        if(dict_["name"] == name_):
            print("<검색하신 수강생은 " + str(i + 1) + "번 입니다.>")
            return 


while(True):
    print("----- 메뉴를 선택하세요 ------")
    print("1. AI 수강생 등록")
    print("2. AI 수강생 목록")
    print("3. AI 수강생 삭제")
    print("4. AI 수강생 수정")
    print("5. AI 수강생 검색")
    print("6. 종료")
    print("")
    input_ = int(input("--->"))

    if(input_ == 1):
        name_ = input("name 을 입력해 주세요 : ")
        age_ = input("age 을 입력해 주세요 : ")
        major_ = input("major 을 입력해 주세요 : ")
        dict_1 = {"name" : name_, "age" : age_, "major" : major_}
        print(register_(dict_1))
    elif(input_ == 2):
        ai_list_()
    elif(input_ == 3):
        name_ = input("삭제할 수강생의 이름을 입력하세요 : ")
        print(ai_remove_(name_))
    elif(input_ == 4):
        name_ = input("수정할 수강생의 이름을 입력하세요 : ")
        age_ = int(input("age 을 입력해 주세요 : "))
        major_ = input("major 을 입력해 주세요 : ")
        dict_1 = {"name" : name_, "age" : age_, "major" : major_}
        print(ai_update_(dict_1))
    elif(input_ == 5):
        name_ = input("검색할 수강생의 이름을 입력하세요 : ")
        ai_search(name_)
    else:
        break

    print("")
    input_ = input("계속하려면 Enter를 치세요")
