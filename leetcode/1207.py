# Given an array of integers arr
# write a function that returns true if and only if the number of occurrences of each value in the array is unique.
def uniqueOccurrences(self, arr: List[int]) -> bool:
    numdict = dict()

    for i in arr:
        if i in numdict:
            numdict[i] += 1
        else:
            numdict[i] = 1

    countList = []

    for count in numdict.values():
        if count not in countList:
            countList.append(count)
        else: 
            return False
    return True