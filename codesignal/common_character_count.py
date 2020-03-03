# Given two strings, find the number of common characters between them.

from collections import Counter

def commonCharacterCount(s1, s2):
    common_letters = Counter(s1) & Counter(s2)  # => {'q': 2, 'r': 1}
    return(sum(common_letters.values()))         # => r