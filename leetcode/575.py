# Given an integer array with even length, where different numbers in this array represent different kinds of candies.
# Each number means one candy of the corresponding kind.
# You need to distribute these candies equally in number to brother and sister.
# Return the maximum number of kinds of candies the sister could gain.

def distributeCandies(self, candies):
    unique_pieces = len(set(candies))
    max_pieces = len(candies) // 2
    
    if unique_pieces > max_pieces:
        return max_pieces
    elif unique_pieces < max_pieces:
        return unique_pieces
    else:
        return max_pieces