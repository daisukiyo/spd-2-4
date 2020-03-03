# Given an arbitrary ransom note string and another string containing letters from all the magazines,
# write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

def canConstruct(self, ransomNote, magazine):
    
    dictionary = {}
    
    for i in magazine:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
            
    for j in ransomNote:
        if j in dictionary and dictionary[j] > 0:
            dictionary[j] -= 1
        else:
            return False
        
    return True
