# Given an array of integers,
# find the maximal absolute difference between any two of its adjacent elements.

def arrayMaximalAdjacentDifference(inputArray):
    max = inputArray[1] - inputArray[0]
    for i in range(len(inputArray) - 1):
        if abs((inputArray[i+1] - inputArray[i])) > max:
            max = abs((inputArray[i+1] - inputArray[i]))
    return max
