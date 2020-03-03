# Ticket numbers usually consist of an even number of digits.
# A ticket number is considered lucky
# if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.
def isLucky(n):
    # consist of an even number of digits
    # luck if sum of first half == sum of second
    digits = list(map(int, str(n)))
    print(digits)
    left_sum = 0
    right_sum = 0

    for i in range(len(digits) // 2):
        left_sum += digits[i]
    
    for i in reversed(range(len(digits) // 2, len(digits))):
        right_sum += digits[i]

    print(left_sum)
    print(right_sum)
    return left_sum == right_sum
