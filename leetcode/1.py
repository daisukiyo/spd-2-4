def twoSum(self, nums, target):
    hashTable = {}
    for i, j in enumerate(nums):
        difference = target - j
        if difference in hashTable:
            return [hashTable[difference], i]
        else:
            hashTable[j] = i