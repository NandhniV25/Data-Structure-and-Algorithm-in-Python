# Accessing/Traversing the list
# Time = O(1) & Space = O(1)
print(" Step 1")
shoppingList = ['Milk', 'Cheese', 'Butter']
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")

# Update/Insert - List 
# Time = O(N) & Space = O(1)
print(" Step 2")
myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15)
myList.append(55)
newList = [11,12,13,14]
myList.extend(newList)
print(myList)

# Slice / Deleting an element in the List
# Time = O(N) & Space = O(1)
# pop returns the deleted element
# delete method cann't return the element 
# but one advantage of using delete method is using the slicing to delete elements
# remove methods don't want to specify the index.we can use the value to be deleted
print(" Step 3")
print(myList[0:2])
myList[0:2] = [2,1]
print(myList)
print(myList.pop(3),myList.pop()) 
print(myList)
del myList[2]
print(myList)
myList.remove(12)
print(myList)

# Searching for an element in the List
# Time = O(N) & Space = O(1)
print(" Step 4")
myList =  [10,20,30,40,50,60,70,80,90]
def searchingList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return f'The {value} does not exist in the list'
print(searchingList(myList, 60))
print(searchingList(myList, 100))