# import numpy as np
# twoDArray = np.array([[1,2,3],[1,2,3],[1,2,3],[1,2,3]])
# print(twoDArray)
# new = np.insert(twoDArray,0,[[1,1,1]],axis=0) #array_name, position, values, row/col
# print(new)


# import numpy as np
# twoDArray = np.array([[1,2,3],[1,2,3],[1,2,3],[1,2,3]])
# print(twoDArray)
#
# def accessElements(array, rowIndex,colIndex):
#     if rowIndex >= len(array) and colIndex >= len(array[0]):
#         print('Incorrect Index')
#     else:
#         print(array[rowIndex][colIndex])
# accessElements(twoDArray,0,0)
# accessElements(twoDArray,1,2)

# import numpy as np
# twoDArray = np.array([[1,2,3],[1,2,3],[1,2,3],[1,2,3]])
# print(twoDArray)
#
# def traverseTwoDArray(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(array[i][j], end=' ')
#         print()
#
# traverseTwoDArray(twoDArray)

import numpy as np
twoDArray = np.array([[1,2,3],[1,2,3],[1,2,3],[1,2,3]])
print(twoDArray)

newTDArray = np.delete(twoDArray, 1,1 )
print(newTDArray)