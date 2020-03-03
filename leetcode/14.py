# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


def longestCommonPrefix(self, strs):
    if not strs:
        return ""

    for index, letter in enumerate(zip(*strs)):
        if len(set(letter)) > 1:
            return(strs[0][:index])
    
    else:
        return min(strs)
    
    