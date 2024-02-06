# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])

# Example
# myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# diagonal_sum(myList2D)


# def diag_sum(arr):
#     sum=0
#     for i in range(0,len(arr)):
#         for j in range(0,len(arr[0])):
#             if(i==j):
#                 sum = sum + arr[i][j]
#     return sum
#
#
# myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(diag_sum(myList2D))

# my_list = [ 84,85,86,87,85,90,85,83,23,45,84,1,2,0 ]
# my_list.sort(reverse=True)
# print(my_list[0:2])

# nums = [1,2,3,1]
# nums.sort()
# for i in range(0,len(nums)):
#     if(nums[i] == nums[i+1]):
#         break
#     print("unique")


# def count_word_frequency(words):
#     words_list = dict()
#     for word in words:
#         words_list[word] = words_list.get(word,0)+1
#     return words_list
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# print(count_word_frequency(words))
