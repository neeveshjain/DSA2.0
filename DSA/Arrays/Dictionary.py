# my_dict = dict()
# print(my_dict)
# eng_sp = dict(one = 'uno', two='dos', three='tres')
# print(eng_sp)
#
# mydict = {'name':'Edy','age':26}
# mydict['age'] = 27
# mydict['address'] = 'kalyani nagar'
# print(mydict)

# traversing
print('-------------')
my_dict = {'name':'Edy','age':26}
def traverseDict(dict):
    for key in dict:
        print(key,dict[key])
traverseDict(my_dict)

def searchDict(dict,value):
    for key in dict:
        if dict[key]==value:
            return key,value
    return False
print(searchDict(my_dict,27))

# del my_dict['age']
print(my_dict)

# removed_element = my_dict.pop('age')

removed_element = my_dict.popitem()
print(removed_element)
print(my_dict)

# Methods
# Method	     Description
# clear()	    -Removes all the elements from the dictionary
# copy()	    -Returns a copy of the dictionary
# fromkeys()	-Returns a dictionary with the specified keys and value
# get()	        -Returns the value of the specified key
# items()	    -Returns a list containing a tuple for each key value pair
# keys()	    -Returns a list containing the dictionary's keys
# pop()	        -Removes the element with the specified key
# popitem()	    -Removes the last inserted key-value pair
# setdefault()	-Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    -Updates the dictionary with the specified key-value pairs
# values()	    -Returns a list of all the values in the dictionary

# def merge_dicts(dict1, dict2):
#     result = dict1.copy()
#     for key, value in dict2.items():
#         result[key] = result.get(key, 0) + value
#     return result
#
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# print(merge_dicts(dict1, dict2))


# def max_value_key(my_dict):
#     max_key =0
#     max_value =0
#     for key,values in my_dict.items():
#         if values>max_value:
#             max_value=values
#             max_key = key
#     return max_key
#
# my_dict = {'a': 5, 'b': 9, 'c': 2}
# print(max_value_key(my_dict))


# def reverse_dict(my_dict):
#     ret_dict = {}
#     for keys,values in my_dict.items():
#         ret_dict[values]=keys
#     return ret_dict
#
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(reverse_dict(my_dict))


# def filter_dict(my_dict, condition):
#     new_dict = {}
#     for key,value in my_dict.items():
#         if condition(key,value):
#             new_dict[key]=value
#     return  new_dict
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
# print(filtered_dict)

# def check_same_frequency(list1,list2):
#     def count_elements(lst):
#         element_count = {}
#         for elem in lst:
#             element_count[elem] = element_count.get(elem,0)+1
#         return element_count
#     return count_elements(list1) == count_elements(list2)
# print(check_same_frequency([1, 2, 3, 2, 1], [3, 1, 2, 1, 3]))
