# Creating an empty dictionary
# Time = O(1) & Space = O(1)
print(" Step 1 ")
d = dict()
d1 = {}
print(d)
print(d1)

# Creating an empty dictionary with elements
# Time = O(N) & Space = O(N)
print(" Step 2 ")
eng_sp = dict(one = "uno", two = "dos")
eng_sp1 = {"one" : 'uno', "two" : 'dos'}
eng_sp_list = [('one','uno'),('two','dos')]
eng_sp_list_dic = dict(eng_sp_list)
print(eng_sp)
print(eng_sp1)
print(eng_sp_list_dic)

# Update / add an element to the dictionary
# Time = O(1) & Space = O(1) => update
# Time = O(1) & Space = amortize O(1) => insert
print(" Step 3 ")
myDict = {'name': 'Edy', 'age': 26}
myDict['address'] = 'London'
myDict['age'] = 27
print(myDict)

# Traverse through a dictionary
# Time = O(N) & Space = O(1)
print(" Step 4 ")
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
traverseDict(myDict)

# Searching a dictionary
# Time = O(N) & Space = O(1)
print(" Step 5 ")
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return f'The {value} does not exist in the given dictionary'
print(searchDict(myDict, 27))
print(searchDict(myDict, 30))

# Delete or remove a dictionary
# Time = O(1) & Space = O(1)
print(" Step 6 ")
del myDict['age']
print(myDict)
removeElement = myDict.pop('name',None) #none is used for error handling. optional
print(removeElement)
print(myDict)
removeElement1 = myDict.popitem() #return key and value
print(removeElement1)
print(myDict)
# Time = O(N) & Space = O(1)
myDict.clear() #delete everything
print(myDict)