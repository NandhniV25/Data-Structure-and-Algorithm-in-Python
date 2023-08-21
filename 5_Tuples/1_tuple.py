# Update and delete cann't perform the operations
a = 5
a_tup = (a,)
# ' '.join(input_tuple) => tuple to string
# How to create a Tuple?
# Time = O(1) & Space = O(N)
print(" Step 1 ")
#  result = tuple( tup[x][x] for x in range(len(tup))) => create another tuple
# return tuple( x for x in tuple1 if x in tuple2)
newTuple = ('a', 'b', 'c', 'd', 'e')
newTuple1 = tuple('abcde')
newTuple2 = ('a', )
newTuple3 = ('a') # it will take as a string not tuples
print(newTuple)
print(newTuple1)
print(newTuple2)
print(newTuple3)

# Access Tuple elements
# Time = O(1) & Space = O(1)
print(" Step 2 ")
print(newTuple[-1]) 
print(newTuple[1:3]) 
print(newTuple[:]) 

# Traverse through tuple
# Time = O(N) & Space = O(1)
print(" Step 3 ")
for i in newTuple:
    print(i)
for index in range(len(newTuple)):
    print(newTuple[index])

# How to search for an element in Tuple?
# Time = O(N) & Space = O(1)
print(" Step 4 ")
print('a' in newTuple)
def searchInTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return f'{pTuple.index(i)} is the index of an element {element}'
    return 'The element does not exist'
print(searchInTuple(newTuple, 'a'))

# Tuple Operations / Functions
print(" Step 5 ")
myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)

print(myTuple + myTuple1) 
print(myTuple * 4)      # repeation 
print(2 in myTuple1)

print(" Step 6 ")
print(myTuple1.count(2))
print(myTuple1.index(2))
print(len(myTuple1))
print(max(myTuple1))
print(min(myTuple1))
print(sum(myTuple1))
print(any(myTuple1))
print(all(myTuple1))
print(sorted(myTuple1))