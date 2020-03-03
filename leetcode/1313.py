
# We are given a list nums of integers representing a list compressed with run-length encoding.

# Consider each adjacent pair of elements [a, b] = [nums[2*i], nums[2*i+1]] (with i >= 0).
# For each such pair, there are a elements with value b in the decompressed list.

# Return the decompressed list.class Solution:

def decompressRLElist(self, nums: List[int]) -> List[int]:
    output = []
    for i in range(len(nums)-1):
        if i%2 == 0:
            output += ([nums[i+1]] * nums[i])
    return(output)
