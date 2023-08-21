import numpy as np

# 1. Create an array with elements  
# Time = O(MN) & Space = O(MN) M=>Coloumns & N=>Rows
print("Step 1")
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

# Insertion using insert() keyword
# axis = 0 => Row 
# axis = 1 => Column  
# Time = O(MN) & Space = O(MN) M=>Coloumns & N=>Rows
# 1 represents position
print("Step 2")
newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
print(newTwoDArray)
print(len(twoDArray))
print(len(newTwoDArray))

# Insertion at last using append() keyword
# axis = 0 => Row 
# axis = 1 => Column  
# Time = O(MN) & Space = O(MN) M=>Coloumns & N=>Rows
print("Step 2.1")
newTwoDArray1 = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray1)
print(len(newTwoDArray1))
print(len(newTwoDArray1[0]))

# Accessing a given cell
# Time = O(1) & Space = O(1) M=>Coloumns & N=>Rows
print("Step 3")
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])
accessElements(newTwoDArray, 1, 2)
accessElements(newTwoDArray, 10, 2)

# Traversing a given array
# Time = O(MN) & Space = O(1) M=>Coloumns & N=>Rows
print("Step 4")
print(twoDArray)
def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=" ")
    print()
traverseTDArray(twoDArray)

# Searching a given value - linear search
# Time = O(MN) & Space = O(1) M=>Coloumns & N=>Rows
print("Step 5")
def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located index '+str(i)+" "+str(j)
    return 'The element is not found'
print(searchTDArray(twoDArray, 444))
print(searchTDArray(twoDArray, 11))

#Deletion using delete() keyword
# Time = O(MN) & Space = O(MN) M=>Coloumns & N=>Rows
print("Step 6")
print(twoDArray)
newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)