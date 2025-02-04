# functions store infor abt car in dict \   always get manufacturer and model name & arbitrary argum
def make_car(manuf, model, **kwargs):
    car_dict = {
        "manufacturer": manuf,
        "model": model,
    }
    car_dict.update(**kwargs)
    return car_dict
# call func with req info and two other name-value pairs 
car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
# print dict 
print(car)