class Entity_1:
    def __init__(self, product_name, product_code, product_description):
        self.product_name = product_name
        self.product_code = product_code
        self.product_description = product_description

    #product_code정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, product_code):
        if(self.product_code == product_code):
            return True
        else:
            return False

    def __str__(self):
        return "{0} : {1} : {2} ".format(self.product_name, self.product_code, self.product_description)


class Entity_2:
    def __init__(self, warehouse_code, product_code, product_num, warehouse_location):
        self.warehouse_code = warehouse_code
        self.product_code = product_code
        self.product_num = product_num
        self.warehouse_location = warehouse_location

    #warehouse_code정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, warehouse_code):
        if(self.warehouse_code == warehouse_code):
            return True
        else:
            return False

    def __str__(self):
        return "{0} : {1} : {2} : {3} ".format(self.warehouse_code, self.product_code, self.product_num, self.warehouse_location)


