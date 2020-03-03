# Given a string, find out if its characters can be rearranged to form a palindrome.

def palindromeRearranging(inputString):
    if len((set(inputString))) <= 1:
        return True
    dict = {}
    for i in list(inputString):
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
    count = 0
    for i in dict.values():
        if i % 2 != 0:
            count += 1
        if count > 1:
            return False
    return True

