# *****
# *****
# *****
# *****
# *****
#
# for i in range(5):
#     for j in range(5):
#         print('*',end='')
#     print()

#-------------------------------------------------------

# *
# **
# ***
# ****
# *****
#
# for i in range(6):
#     for j in range(i):
#         print('*',end='')
#     print()

#-------------------------------------------------------

# 1
# 12
# 123
# 1234
# 12345
#
# for i in range(6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

#-------------------------------------------------------

# 1
# 22
# 333
# 4444
# 55555
#
# for i in range(6):
#     for j in range(1,i+1):
#         print(i,end='')
#     print()

#-------------------------------------------------------

# *****
# ****
# ***
# **
# *
#
# for i in range(5,0,-1):
#     for j in range(i):
#         print('*',end='')
#     print()

#-------------------------------------------------------

# 12345
# 1234
# 123
# 12
# 1
#
# for i in range(5,0,-1):
#     for j in range(i):
#         print(j+1,end='')
#     print()

#-------------------------------------------------------

#     *
#    ***
#   *****
#  *******
# *********

# num_rows = 5
#
# for i in range(num_rows):
#     for j in range(num_rows - i - 1):
#         print(" ", end="")
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print()

# -------------------------------------------------------


# ***********
#  *********
#   *******
#    *****
#     ***
#      *

# num_rows = 5
# for i in range(num_rows, 0, -1):
#     for j in range(num_rows - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()

