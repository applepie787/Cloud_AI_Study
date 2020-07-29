import service

class DataController:

    def register_controller(self, IDcode, entity, table_name):

        if IDcode == "" or IDcode == 0 : 
            return "ID코드 형식이 잘못됐습니다."
        else:
            bm = service.CommunityService()
            message = bm.register(entity, table_name)
            return message

    def get_all_entity_controller(self, table_name, ID_, key_name):
        bm = service.CommunityService()
        list_ = bm.get_all_entity(table_name, ID_, key_name)
        return list_

    def update_controller(self, IDcode, entity, table_name):
        if IDcode == "" or IDcode == 0 :
            return "ID코드 형식이 잘못됐습니다."
        else:
            bm = service.CommunityService()
            message = bm.entity_update(entity, table_name)
            return message
    
    def delete_controller(self, IDcode, table_name):
        if IDcode == "" or IDcode == 0 :
            return "ID코드 형식이 잘못됐습니다." 
        else:
            bm =service.CommunityService()
            message = bm.entity_remove(IDcode, table_name)
            return message

    # def get_entity_controller(self, IDcode, table_name):
    #     if IDcode == "" or IDcode == 0 :
    #         return "ID코드 형식이 잘못됐습니다."        
    #     else:
    #         bm =service.CommunityService()
    #         product_entity = bm.get_product_entity(IDcode, table_name)
    #         if product_entity != None :
    #             return product_entity
    #         else:
    #             return "존재하지 않습니다." 

    def close(self):
        bm=service.CommunityService()
        bm.close()
    


            