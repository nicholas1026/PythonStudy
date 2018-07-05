class Restaurant():
    """一个简单的餐馆类"""

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant name is:"+self.restaurant_name+" and it's cuisine type is:"+self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant "+self.restaurant_name+" is opening")

class IceCreamStand(Restaurant):
    """一个继承restaurant类的子类"""

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.favors = ['Vanilla','Strawberry']

    def describe_icecream_favors(self):
        print("These icecream  are :")
        for icecream in self.favors:
            print("The "+icecream+" icecream")


my_ice_cream=IceCreamStand('hillton','five starts')
my_ice_cream.describe_icecream_favors()
