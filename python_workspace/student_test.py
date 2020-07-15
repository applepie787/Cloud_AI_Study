class Person_:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, id):
        if(self.id == id):
            return True
        else:
            return False

    def info(self):
        print("아이디 : {0}\t이름 : {1}\t".format(self.id, self.name), end="")

class Student_(Person_):
    def __init__(self, id, name, major):
        Person_.__init__(self, id, name)
        self.major = major

    def student_info(self):
        super().info()
        print("전공 : {0}".format(self.major))

class Teacher_(Person_):
    def __init__(self, id, name, subject):
        super().__init__(id, name)
        self.subject = subject

    def teacher_info(self):
        super().info()
        print("과목 : {0}".format(self.subject))

class Employee_(Person_):
    def __init__(self, id, name, department):
        super().__init__(id, name)
        self.department = department

    # def employee_info(self):
    #     print("사번 : {0}\t이름 : {1}\t부서 : {2}".format(self.id, self.name, self.department))
    def info(self):
        print("사번 : {0}\t이름 : {1}\t부서 : {2}".format(self.id, self.name, self.department))


