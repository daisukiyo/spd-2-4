# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

def countSubstrings(self, s):

    count = 0
    
    for i in range(len(s)):
        j = 0
        while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]:
            count += 1
            j += 1
        j = 0
        while i-j >= 0 and i+j+1 < len(s) and s[i-j] == s[i+j+1]:
            count += 1
            j += 1
            
    return count
                
                