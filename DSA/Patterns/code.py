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

# -------------------------------------------------------

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
#
# for i in range(5):
#     for j in range(i):
#         print('*',end='')
#     print()
# for k in range(5,0,-1):
#     for l in range(k):
#         print('*',end='')
#     print()

# -------------------------------------------------------

# 1
# 01
# 101
# 0101
#
# n = 5
# for i in range(0,n):
#     for j in range(0,i):
#         if i == j :
#             print(0,end='')
#         elif (i%2 == 1 and j%2 == 0):
#             print(1,end='')
#         elif (i%2 == 0 and j%2 == 0):
#             print(0,end='')
#         elif (i%2 == 0 and j%2 == 1):
#             print(1,end='')
#         elif (i%2 == 1 and j%2 == 1):
#             print(0 ,end='')
#     print()
#
# #Optimised version
# n = 5
# for i in range(n):
#     for j in range(i):
#         # Determine the value to print based on the parity of i and j
#         if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
#             print(0, end='')
#         else:
#             print(1, end='')
#     print()
# -------------------------------------------------------

# 1      1
# 12    21
# 123  321
# 12344321
# n = 5
# for i in range(n):
#     for j in range(1,i+1):
#         print(j,end='')
#     for k in range(2*(n-i-1)):
#         print(' ',end='')
#     for l in range(i,0,-1):
#         print(l,end='')
#     print()

# -------------------------------------------------------

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# n = 6
# count = 1
# for i in range(n):
#     for j in range(i):
#         print(count,end=' ')
#         count += 1
#     print()

# -------------------------------------------------------

# A
# AB
# ABC
# ABCD
# ABCDE
#
# char = 65
# n = 6
# for i in range(n):
#     for j in range(i):
#         print(chr(char),end='')
#         char += 1
#     char = 65
#     print()

# -------------------------------------------------------

# ABCDE
# ABCD
# ABC
# AB
# A
# char = 65
# n = 5
#
# for i in range(n,0,-1):
#     for j in range(i):
#         print(chr(char),end='')
#         char += 1
#     char = 65
#     print()

# -------------------------------------------------------

# A
# BB
# CCC
# DDDD
# EEEEE
#
# char = 64
# n = 6
# for i in range(0,n):
#     for j in range(0,i):
#         print(chr(char),end='')
#     char += 1
#     print()

# -------------------------------------------------------

#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA
#
# n = 5
#
# for i in range(n):
#     for j in range(n - i - 1):
#         print(' ', end='')
#     char = 65
#     breakpr = (2 * i + 1) // 2
#     for k in range(2 * i + 1):
#         print(chr(char), end='')
#         if k < breakpr:
#             char += 1
#         else:
#             char -= 1
#     print()

# -------------------------------------------------------


# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********
#
# n = 5
# for i in range(n):
#     for j in range(n -i -1):
#         print('*',end='')
#     for k in range(2*i+1):
#         print(' ',end='')
#     for j in range(n -i -1):
#         print('*',end='')
#     print()
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print('*',end='')
#     for k in range(2*i+1):
#         print(' ',end='')
#     for j in range(n-i):
#         print('*',end='')
#     print()
#
# n = 5
# # Upper part of the pattern
# for i in range(n):
#     # Print leading stars
#     for j in range(n - i):
#         print('*', end='')
#     # Print spaces
#     for k in range(2 * i):
#         print(' ', end='')
#     # Print trailing stars
#     for j in range(n - i):
#         print('*', end='')
#     print()
#
# # Lower part of the pattern
# for i in range(n):
#     # Print leading stars
#     for j in range(i + 1):
#         print('*', end='')
#     # Print spaces
#     for k in range(2 * (n - i - 1)):
#         print(' ', end='')
#     # Print trailing stars
#     for j in range(i + 1):
#         print('*', end='')
#     print()

# -------------------------------------------------------

# *      *
# **    **
# ***  ***
# ********
# ***  ***
# **    **
# *      *
#
# n = 5
# for i in range(n):
#     for j in range(i):
#         print('*',end='')
#     for k in range(2*(n-i-1)):
#         print(' ',end='')
#     for l in range(i):
#         print('*',end='')
#     print()
# for i in range(n-2,0,-1):
#     for j in range(i):
#         print('*',end='')
#     for k in range(2*(n-i-1)):
#         print(' ',end='')
#     for l in range(i):
#         print('*',end='')
#     print()

# -------------------------END------------------------------