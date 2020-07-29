from _exception import DuplicateException, RecordNotFoundException
from store import DBStore
from domain import MemberEntity, ClubEntity, MemberShipEntity 


def table_name_check(entity, table_name):
    if(table_name == "club_"):
        IDcode = entity.clubID
        name = entity.name
    elif(table_name == "member_"):
        IDcode = entity.email
        name = entity.name
    elif(table_name == "membership_"):
        IDcode = entity.membershipID
        name = entity.membershipID

    return (IDcode, name)

class CommunityService:
    db = DBStore()
  
    #Emtity 등록 : key_ID 존재여부 체크
    def register(self, entity, table_name):
        (IDcode, name) = table_name_check(entity, table_name)
        result= self.is_exist(IDcode, table_name)
        
        if not bool(result):
            CommunityService.db.insert(entity, table_name)
            return str(name) + "가 등록되었습니다."
        else:
            try:
                raise DuplicateException(name)  
            except DuplicateException as error:
                return str(error)


    def get_all_entity(self, table_name, ID_, key_name):
        return CommunityService.db.select_records(table_name, ID_, key_name)

    #Entity 정보 수정
    def entity_update(self, entity, table_name):
        (IDcode, name) = table_name_check(entity, table_name)
        result= self.is_exist(IDcode, table_name)

        if bool(result) :
            CommunityService.db.update(entity, table_name)
            return str(name) + " 정보수정 되었습니다."
        else:
            try:
                raise RecordNotFoundException(name)
            except RecordNotFoundException as updateError:
                return str(updateError)
    
    #Entity 등록 정보 삭제
    def entity_remove(self, IDcode, table_name):

        result= self.is_exist(IDcode, table_name)
        if bool(result):
            CommunityService.db.delete(IDcode, table_name)
            return str(IDcode) + " 삭제 되었습니다."
        else:
            try:
                raise RecordNotFoundException(IDcode)
            except RecordNotFoundException as removeError:
                return str(removeError)
           
    # #Entity 상세 정보
    # def get_product_entity(self, IDcode, table_name):
    #     result = self.is_exist(IDcode, table_name)
    #     if bool(result):
    #         if(table_name == "club_"):
    #             return ClubEntity(result['clubID'], result['name'], result['phone_number'], result['foundation_date'], result['address'])
    #         elif(table_name == "member_"):
    #             return MemberEntity(result['email'], result['name'], result['phone_number'], result['birthday'])
    #         elif(table_name == "membership_"):
    #             return MemberShipEntity(result['membershipID'], result['clubID'], result['member_email'], result['join_date'], result['role_in_club'])
            
    #     else:
    #         try:
    #             raise RecordNotFoundException(IDcode)
    #         except RecordNotFoundException as searchError:
    #             return str(searchError)
                
    # Entity 존재여부
    def is_exist(self, IDcode, table_name):
        result = CommunityService.db.select_by_product_code(IDcode, table_name)
        return result

    def close(self):
        CommunityService.db.close()
