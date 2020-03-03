# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

def isPalindrome(self, x):
    if x<0 or x != int(str(abs(x))[::-1]):
        return False
    else:
        return True
        