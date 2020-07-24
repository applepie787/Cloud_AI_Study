import controller_
from domain import Entity_1
from product_view import menu_display, input_select_menu, input_product_code, input_product_entity, message_display
controller = controller_.ProductController()


while True:
   
    menu_display()

    menu = input_select_menu()
    if menu == '1':
        product_code = input_product_code()
        product_name, product_description = input_product_entity()        
        controller.register_controller(Entity_1(product_name, product_code, product_description))
        
    elif menu == '2':
        controller.get_all_entity_controller()

    elif menu == '3':
        product_code = input_product_code()
        product_name, product_description = input_product_entity()
        controller.update_controller(Entity_1(product_name, product_code, product_description))
   
    elif menu == '4':
        product_code = input_product_code()
        controller.delete_controller(product_code)

    elif menu == '5':
        product_code = input_product_code()
        controller.get_entity_controller(product_code)
               
    elif menu =='0':
        controller.close()
        break
    else:
        message_display("메뉴는 1,2,3,4,5 중 하나를 선택하시고 종료를 원하시면 0번을 선택하세요")
    continue