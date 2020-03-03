# Given matrix, a rectangular matrix of integers
# where each value represents the cost of the room
# your task is to return the total sum of all rooms
# that are suitable for the CodeBots
# (ie: add up all the values that don't appear below a 0).

def matrixElementsSum(matrix):
    r = len(matrix) # 3
    c = len(matrix[0]) # 4
    sum = 0
    for i in range(r):
        for j in range(c):
            if i>0 and matrix[i-1][j] == 0:
                matrix[i][j] = 0
                sum += 0
            else:
                sum += (matrix[i][j])
    return sum