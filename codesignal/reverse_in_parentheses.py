# Write a function that reverses characters in (possibly nested)
# parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

def reverseInParentheses(inputString):
    length = len(inputString)

    if '(' and ')' not in list(inputString):
        return inputString

    close_index = inputString.rfind(")")

    for i in reversed(range(0, close_index)):
        if inputString[i] == ")":
            close_index = i
        if inputString[i] == "(":
            sub = inputString[i+1:close_index][::-1]
            new = inputString[0:i] + sub + inputString[close_index+1:]
            return reverseInParentheses(new)