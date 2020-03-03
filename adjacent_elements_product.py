# Given an array of integers
# find the pair of adjacent elements that has the largest product
# and return that product.

def adjacentElementsProduct(inputArray):
    max_product = inputArray[0] * inputArray[1]
    for i in range(len(inputArray)-1):
        if (inputArray[i] * inputArray[i+1]) > max_product:
            max_product = inputArray[i] * inputArray[i+1]
    return max_product