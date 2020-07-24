from product_view import message_display, product_list_display, product_entity_display
import service

#view 입력된 데이터 체크, service의 business method 호출, 호출된 결과값 저장, view select
class ProductController:

    def register_controller(self, entity):
        #상품코드 valid check - regular express사용  상품코드 형식 체크
        if entity.product_code == "" or entity.product_code == 0 :
            message_display("제품코드 형식이 잘못됐습니다.")
        else:
            #business method delegation
            bm = service.ProductService()
            message = bm.register(entity)
            #view select
            message_display(message)

    def get_all_entity_controller(self):
        bm = service.ProductService()
        product_list = bm.get_all_entity()
        product_list_display(product_list)

    def update_controller(self,entity):
        if entity.product_code == "" or entity.product_code == 0 :
            #error view select
            message_display("제품 코드 형식이 잘못됐습니다.")
        else:
            #business method delegation
            bm = service.ProductService()
            message = bm.entity_update(entity)
            #view select
            message_display(message)
    
    def delete_controller(self, product_code):
        if product_code == "" or product_code == 0 :
            message_display("제품 코드 형식이 잘못됐습니다.") 
        else:
            bm =service.ProductService()
            message = bm.entity_remove(product_code)
            message_display(message)

    def get_entity_controller(self, product_code):
        if product_code == "" or product_code == 0 :
            message_display("제품 코드 형식이 잘못됐습니다.")        
        else:
            bm =service.ProductService()
            product_entity = bm.get_product_entity(product_code)
            if product_entity != None :
                product_entity_display(product_entity)
            else:
                message_display("존재하지 않습니다.") 

    def close(self):
        bm=service.ProductService()
        bm.close()
    


            