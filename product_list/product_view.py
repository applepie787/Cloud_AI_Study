#View : 입력하는 화면제공, 결과값 출력
#메뉴 출력
def menu_display():
    print("====  상품 등록 관리 프로그램 =====")
    print("1. 상품 정보 등록")
    print("2. 상품 목록")
    print("3. 상품 정보 수정")
    print("4. 상품 삭제")
    print("5. 상품 정보 검색")
    print("0. 종료")


#message출력
def message_display(message):
    print(message)


#product_list목록 출력
def product_list_display(product_list):
    print("==== 등록 상품 목록 ===")
    for value in product_list:
        print("{0}".format(str(value)) )

#product_entity 상세정보 출력
def product_entity_display(product_entity):
    # print("{0} 상세정보 : {1}".format(ai_entity.email, str(ai_entity)) )
    print("상세정보 : {0}".format(product_entity))


#구분선
def line_dispay():
    print("="*30)

#product_entity 정보입력
def input_product_entity():
    product_name = input("상품이름 : ")
    product_description = input("상품설명 : ")
    return product_name, product_description

def input_product_code():
    product_code =  int(input("상품코드 : "))
    return product_code

#menu select  정보 입력
def input_select_menu():
    menu = input("항목을 선택하세요 ")
    return menu