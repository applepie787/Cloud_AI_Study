import ai_controller
from domain import AIEntity
from ai_view import menu_display,input_select_menu,input_email,input_ai_entity,message_display
controller = ai_controller.AIController()


while True:
   
    menu_display()

    menu = input_select_menu()
    if menu == '1':
        email =input_email()
        name,age,major = input_ai_entity()        
        controller.register_controller(AIEntity(name, age, email, major))
        
    elif menu == '2':
        controller.get_all_entity_controller()

    elif menu == '3':
        email = input_email()
        name,age,major = input_ai_entity()
        controller.update_controller(AIEntity(name, age, email, major))
   
    elif menu == '4':
        email = input_email()
        controller.delete_controller(email)

    elif menu == '5':
        email = input_email()
        controller.get_entity_controller(email)
               
    elif menu =='0':
        controller.close()
        break
    else:
        message_display("메뉴는 1,2,3,4,5 중 하나를 선택하시고 종료를 원하시면 0번을 선택하세요")
    continue