# Given a string, find out if it satisfies the IPv4 address naming rules.

def isIPv4Address(inputString):
    inputString = inputString.split('.')
    print(inputString)
    if len(inputString) != 4:
        return False
    for i in inputString:
        try:
            x = int(i)
            if x > 255 or x < 0:
                return False
        except ValueError:
            return False
    return True
