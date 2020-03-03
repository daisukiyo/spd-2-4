# Given a sequence of integers as an array, determine whether it is possible to obtain 
# a strictly increasing sequence by removing no more than one element from the array.

def check_increasing(seq):
    # This will check if it is increasing:
    # If it is return -1 else return the element at which is it not increasing
    for i in range(len(seq)-1):
        if seq[i] >= seq[i+1]:
            return i
    return -1

def almostIncreasingSequence(sequence):
    check = check_increasing(sequence)
    # List is increasing
    if check == -1:
        return True
    # Check if removing an item will make a strictly increasing list
    if check_increasing(sequence[check-1:check] + sequence[check+1:]) == -1 or check_increasing(sequence[check:check+1] + sequence[check+2:]) == -1:
        return True
    # If not return False, since more than 1 element needs to be removed
    return False

