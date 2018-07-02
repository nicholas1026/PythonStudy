def make_car(maker,type,**cars_info):
    cars={}
    cars['maker']=maker
    cars['type']=type
    for key,value in cars_info.items():
        cars[key]=value

    return cars

car=make_car('audo','Q7',color='black',kind='SUV',matcidriver=4,price=1000000)
print(car)
