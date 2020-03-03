# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

# If the last word does not exist, return 0.

def lengthOfLastWord(self, s):

    words = s.split()
    if not words:
        return 0
    
    return len(words[-1])