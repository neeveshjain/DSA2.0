# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# def sum_product(input_tuple):
#     sum = 0
#     product =1
#     for i in range(len(input_tuple)):
#         sum = sum + input_tuple[i]
#         product = product * input_tuple[i]
#     return sum,product
#
# input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, ' ',product_result)

# def insert_value_front(input_tuple, value_to_insert):
#     new_tuple = (value_to_insert,) + input_tuple
#     return new_tuple
#
# input_tuple = (2, 3, 4)
# value_to_insert = 1
# output_tuple = insert_value_front(input_tuple, value_to_insert)
# print(output_tuple)

# def concatenate_strings(input_tuple):
#     output_string = ' '.join(input_tuple)
#     return output_string
#
# input_tuple = ('Hello', 'World', 'from', 'Python')
# output_string = concatenate_strings(input_tuple)
# print(output_string)
#

# def get_diagonal(tup):
#     sum=0
#     for i in range(len(tup)):
#         for j in range(len(tup)):
#             if(i==j):
#                 sum = sum + tup[i][j]
#     return sum
#
# input_tuple = (
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9)
# )
# output_tuple = get_diagonal(input_tuple)
# print(output_tuple)  # Expected output: (1, 5, 9)

# def common_elements(tuple1, tuple2):
#     sol = ()
#     for i in range(len(tuple1)):
#         for j in range(len(tuple2)):
#             if tuple1[i] == tuple2[j]:
#                 sol = sol + (tuple1[i],)
#     return sol
#
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (4, 5, 6, 7, 8)
# output_tuple = common_elements(tuple1, tuple2)
# print(output_tuple)  # Expected output: (4, 5)
