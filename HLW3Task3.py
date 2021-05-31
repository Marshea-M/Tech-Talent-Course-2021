import numpy as np
my_task_array=np.array([0,1,2,3,4,5,6,7,8,9])
print(my_task_array)

#an array with only boolean True values
boolean_array=np.array([[(1,2,3),(4,5,6),(7,8,9)]],dtype=float)
print(boolean_array)

import numpy as np
extract_arr=np.array([1,2,3,4,5,6,7,8,9,10])
print("Array from 1-10  ", extract_arr)

odd=np.where(extract_arr%2!=0)
extract_arr=np.delete(extract_arr,odd)
print("After extracting all odd numbers:  ", extract_arr)

import numpy as np
replace_arr=np.array([1,2,3,4,5,6,7,8,9,10])
print("Array from 1-10  ", replace_arr)

print("Replacing all odd numbers with -1:  ", np.where(replace_arr%2!=0,-1, replace_arr))


#convert a 1D array to a 2D array with 2 rows

array5=np.array([7,9,13,23,5,67,9,2,14,50,48,40,62,39])
print("This is the 1D array:    ")
print(array5)
reshapedarray5=array5.reshape(1,2,7)
#Now a 2D array 1 matrix, 2 rows, 7 columns

print("This is the reshaped array:   ")
print(reshapedarray5)


#create two arrays a and b, stack these two arrays vertically use the np.dot and np.sum to calculate totals

Array_A=np.array([100,230,178,905,321,764,340])
Array_B=np.array([270,500,140,390,810,650,400])


#stack the two arrays
print ("Two arrays stacked together")
print(np.vstack((Array_A,Array_B)))

#multiply the two arrays vertically

Array_C=np.dot(Array_A,Array_B)
print("Multiplying the two arrays:  ")
print(Array_C)

#add the teo arrays vertically
Array_D=np.sum((Array_A,Array_B),axis=0)
print("Adding the two arrays:   ")
print(Array_D)
