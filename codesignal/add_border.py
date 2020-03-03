# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

def addBorder(picture):
    row = len(picture)
    column = len(picture[0]) + 2
    for i in range(len(picture)):
        picture[i] = "*" + picture[i] + "*"
    picture.insert(0, column * '*')
    picture.append(column * '*')
    return picture