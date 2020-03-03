# You are given an array of integers.
# On each move you are allowed to increase exactly one of its element by one.
# Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

def arrayChange(inputArray):
    moves = 0
    total_moves = 0
    for i in range(len(inputArray)-1):
        if inputArray[i] >= inputArray[i+1]:
            moves = (inputArray[i] - inputArray[i+1] + 1)
            total_moves += moves
            inputArray[i+1] += moves
    return total_moves