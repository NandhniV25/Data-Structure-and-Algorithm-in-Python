import array

arr = array.array('i')
print(arr)

arr1 = array.array('i', [1,2,3,4,5])
print(arr1)

import numpy as np

np_arr = np.array([], dtype=int) 
print(np_arr)

np_arr1 = np.array([1,2,3,4,5])
print(np_arr1)

#No memory allocated for the empty array by using numpy
#Numpy => faster mathematical calculation
#both numpy and array has same time O(N) and space complexity O(N) for creating the array elements
#both numpy and array has same time O(1) and space complexity O(1) for initializing the array elements