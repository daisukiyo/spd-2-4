# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number
# For the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

def fizzBuzz(self, n):
    result = []
    for i in range(1, n+1):
        value = str(i)
        if i % 3 == 0 and i % 5 == 0:
            value = "FizzBuzz"
        elif i % 3 == 0:
            value = "Fizz"
        elif i % 5 == 0:
            value = "Buzz"
        result.append(value)

    return result