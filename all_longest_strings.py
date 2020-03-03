# Given an array of strings
# return another array containing all of its longest strings.

def allLongestStrings(inputArray):
    result = {}
    for word in inputArray:
        result.setdefault(len(word),[]).append(word)
    longest_count = sorted(result.keys())[-1]
    return result[longest_count]
