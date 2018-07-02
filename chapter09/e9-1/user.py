class User():
    """创建一个user类"""
    def __init__(self,first_name,last_name,sex,age):
        self.first_name=first_name
        self.last_name=last_name
        self.sex=sex
        self.age=age

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.sex)
        print(self.age)


my_user=User("yunfei","xi","Man",32)
my_user.describe_user()
