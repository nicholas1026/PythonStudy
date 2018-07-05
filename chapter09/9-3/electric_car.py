class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometre(self):
        print("This car has "+str(self.odometre_reading)+" miles on it" )

    def update_odometre(self,mileage):
        if mileage >= self.odometre_reading:
            self.odometre_reading = mileage
        else:
            print("You can't roll back an odometre!")

    def increment_odometre(self,miles):
        self.odometre_reading += miles

    def fill_gas_tank(self):
        print("Let's file the car with gas!")


class ElectricCar(Car):
    """独特的电动汽车"""
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        print("This can has a "+str(self.battery_size)+"-kWh Battery.")

    def fill_gas_tank(self):
        print("The car "+self.get_descriptive_name()+"doesn't need a gas tank")



my_tesla = ElectricCar('tesla','model S',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
