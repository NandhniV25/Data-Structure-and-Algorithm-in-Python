# key in dictionary => in operator works with keys. default it checks keys not values
# values in dictionary.values() => in operator works with values
# not in operator similar to in operator

# len(dictionary) => counting the no of pairs in the dictionary
# max(my_dict, key=my_dict.get) => returns the maximum value of the key in the dictionary

# all(dictionary) => returns boolean value 
# => 1.All keys are True => True
# => 2.All keys are False => False
# => 3.one key is True => False

# any(dictionary) => returns boolean value 
# => 1.All keys are True => True
# => 2.All keys are False => False
# => 3.one key is True => True

# sorted(dictionary) => return the list of the keys in the sorted order

my_dict = {
    1 : "one",
    3 : "three",
    5 : "five",
    1 : "one",
    9 : "nine"
}
print(all(my_dict))

# Sorted method
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}
print(sorted(myDict, key=len))
print(sorted(myDict))