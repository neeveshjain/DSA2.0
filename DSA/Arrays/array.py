# import array
# my_array = array.array('i',[1,2,3,4])
# print(my_array)
# import numpy as np
# my_array = np.array([[1,2,3],[2,3,4]],dtype=int)
# print(my_array)

# import array
# arr = array.array('i',[1,2,3,4])
# print(arr)
# arr.insert(0,6)
# print(arr)
# n = len(arr)
# for i in range (n):
#     print(arr[i])

# import array
# arr = array.array('i',[1,2,3,4])
# print(arr)
#
# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#     return -1
# print(linear_search(arr,6))

import array

#Create an array and traverse

my_array = array.array('i',[1,2,3,4])
for i in my_array:
    print(i)

#Access individual elements from the array
print("Step 2")
print(my_array[1])

#Append any value to the array using append() method
print("Step 3")
my_array.append(6)
print(my_array)

#Insert value in the array using insert() method
print("Step 4")
my_array.insert(0,3)
print(my_array)

#Extend python array using extend() method
print("Step 5")
my_array1 = array.array('i',[7,8,9])
my_array.extend(my_array1)
print(my_array)

#Add items from list in to array using fromlist()method
print("Step 6")
templist = [15,16,17]
my_array.fromlist(templist)
print(my_array)

#Remove any array element using remove() method
print("Step 7")
my_array.remove(15)
print(my_array)

#Remove last array alement using pop() method
print("Step 8")
my_array.pop()
print(my_array)

#Fetch any element through its index using index() method
print("Step 9")
print(my_array.index(6))

#Reverse a python array using reverse function
print("Step 10")
my_array.reverse()
print(my_array)

#get array buffer information through buffer_info() method
print("Step 11")
print(my_array.buffer_info())

#check for the number of occurance of an element using count() method
print("Step 12")
print(my_array.count(3))

#convert array in to string using to_method()
print("Step 13")
# strTemp = my_array.tostring()
# print(strTemp)

print("Step 14")
print(my_array.tolist())

print("Step 15")
print(my_array[1::4])