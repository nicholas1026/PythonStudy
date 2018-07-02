class Restaurant():
    """一个简单的餐馆类"""

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant name is:"+self.restaurant_name+" and it's cuisine type is:"+self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant "+self.restaurant_name+" is opening")

restaurant=Restaurant('香格里拉','五星级')
restaurant1=Restaurant('丽兹卡尔顿','五星级')
restaurant2=Restaurant('希尔顿','五星级')

restaurant.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

restaurant.open_restaurant()
