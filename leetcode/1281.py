# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

def subtractProductAndSum(self, n: int) -> int:
    prod = 1
    list_of_nums = list(map(int, str(n)))
    for i in list_of_nums:
        prod = prod * i
    diff = prod - sum(list_of_nums)
    return diff