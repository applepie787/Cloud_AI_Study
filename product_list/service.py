from _exception import DuplicateException, RecordNotFoundException
from store import ProductStore
from domain import Entity_1 

class ProductService:
    #AIEntuty 정보를 저장하는 클래스 변수
    # ai_list =[]
    db = ProductStore()
  
    #수강생등록 : email 존재여부 체크
    def register(self, entity):
        result= self.is_exist(entity.product_code)
        if not bool(result):
            ProductService.db.insert(entity)
            return entity.product_name + "가 등록되었습니다."
        else:
            try:
                raise DuplicateException(entity.product_name)  
            except DuplicateException as error:
                return str(error)


    def get_all_entity(self):
        return ProductService.db.select_all()

    #제품 정보 수정
    def entity_update(self,entity):
        result = self.is_exist(entity.product_code)
        if bool(result) :
            ProductService.db.update(entity)
            return entity.product_name + " 정보수정 되었습니다."
        else:
            try:
                raise RecordNotFoundException(entity.product_name)
            except RecordNotFoundException as updateError:
                return str(updateError)
    
    #제품 등록 정보 삭제
    def entity_remove(self,product_code):
        result = self.is_exist(product_code)
        if bool(result):
            ProductService.db.delete(product_code)
            return str(product_code) + " 삭제 되었습니다."
        else:
            try:
                raise RecordNotFoundException(product_code)
            except RecordNotFoundException as removeError:
                return str(removeError)
           
    #제품 상세 정보
    def get_product_entity(self,product_code):
        result = self.is_exist(product_code)
        if bool(result):
            return Entity_1(result['product_name'], result['product_code'], result['product_description'])
        else:
            try:
                raise RecordNotFoundException(product_code)
            except RecordNotFoundException as searchError:
                return str(searchError)
                
    #제품 코드 존재여부
    def is_exist(self,product_code):
        result = ProductService.db.select_by_product_code(product_code)
        return result

    def close(self):
        ProductService.db.close()
