# Syntax

# dictionary.clear() => delete everything
# dictionary.popitem() => delete last item. return key and value
# dictionary.pop(key, value) => returns key_value. value(optional) is used for error handling 

# dictionary.copy() => doesn't modify the original dictionary. creates new dictionary

# dictionary.fromkeys(sequence[], value) => value optional parameter(None by default). creates new dictionary. 
# dictionary.get(key, value)
# dictionary.setdefault(key, default_value) => if key exists returns value otherwise set key and default value

# dictionary.items() => returns tuple pairs
# dictionary.keys() => returns list contains keys
# dictionary.values() => returns list contains values

# dictionary.update(other_dictionary or tuple) => combine both dictionary like extend method



newDict = {}.fromkeys([1,2,3],0)
print(newDict)

mydict = {'name': 'Edy', 'age': 26}
print(mydict.get('age',27))