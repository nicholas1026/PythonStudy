class User():
    """创建一个user类"""
    def __init__(self,first_name,last_name,gender,age):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.age=age

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.gender)
        print(self.age)


class Admin(User):
    def __init__(self,first_name,last_name,gender,age):
        super().__init__(first_name,last_name,gender,age)
        self.privileges = ['can add post','can delete post','can ban user']


    def show_privileges(self):
        print("The administrator has:")
        for privilege in self.privileges:
            print(privilege)


ad = Admin('yunfei','xi','male',33)
ad.show_privileges()
