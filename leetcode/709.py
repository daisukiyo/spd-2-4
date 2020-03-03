# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

def toLowerCase(self, str: str) -> str:
    lowercase = ''
    for char in str:
        # ord returns an integer representing unicode
        if ord(char) >= 65 and ord(char) <= 90:
            # chr returns a character from unicode
            lowercase += chr(ord(char)+32)
        else:
            lowercase += char

    return lowercase