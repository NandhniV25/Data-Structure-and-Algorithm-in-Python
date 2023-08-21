# new_dict = {new_key : new_value for item in list/dict}
# new_dict = {new_key : new_value for (key/value) in dict.items()}
# new_dict = {new_key : new_value for (key/value) in dict.items() if condition}
# new_dict = {k: v for k, v in my_dict.items() if condition(k, v)} -> filter_dict(my_dict, lambda k, v: v % 2 == 0) -> method 

import random

city_names = ['Paris', 'Bangkok', 'Pattaya', 'London']
city_temps = {city : random.randint(20,30) for city in city_names}
print(city_temps)
city_high_temps = {city : temp for city, temp in city_temps.items() if temp > 25}
print(city_high_temps)