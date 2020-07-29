
class MemberEntity:
    #생성자정의 : member variable - email, name, phone_number, birthday 초기화
    def __init__(self, email, name, phone_number, birthday):
        self.email = email
        self.name = name
        self.phone_number = phone_number 
        self.birthday = birthday

    #email정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, email):
        if(self.email == email):
            return True
        else:
            return False
    # phone_number의 경우 개인 정보
    def __str__(self):
        return "{0} : {1} : {2} ".format(self.email, self.name, self.birthday)


class ClubEntity:
    #생성자정의 : member variable - clubID, name, phone_number, foundation_date, address 초기화
    def __init__(self, clubID, name, phone_number, foundation_date, address):
        self.clubID = clubID
        self.name = name
        self.phone_number = phone_number
        self.foundation_date = foundation_date
        self.address = address 

    #clubID정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, clubID):
        if(self.clubID == clubID):
            return True
        else:
            return False

    def __str__(self):
        return "{0} : {1} : {2} : {3} : {4} ".format(self.clubID, self.name, self.phone_number, self.foundation_date, self.address)



class MemberShipEntity:
    #생성자정의 : member variable - membershipID, clubID, member_email, join_date, role_in_club 초기화
    def __init__(self, membershipID, clubID, member_email, join_date, role_in_club):
        self.membershipID = membershipID
        self.clubID = clubID
        self.member_email = member_email
        self.join_date = join_date
        self.role_in_club = role_in_club

    #membershipID정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, membershipID):
        if(self.membershipID == membershipID):
            return True
        else:
            return False

    def __str__(self):
        return "{0} : {1} : {2} : {3} : {4} ".format(self.membershipID, self.clubID, self.member_email, self.join_date, self.role_in_club)


