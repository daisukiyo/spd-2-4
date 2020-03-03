# Some people are standing in a row in a park.
# There are trees between them which cannot be moved.
# Your task is to rearrange the people by their heights
# in a non-descending order without moving the trees. People can be very tall!

def sortByHeight(a):

    indices = []

    for i, val in enumerate(a):
        if val == -1:
            indices.append(i)
    
    a.sort()

    length = len(indices)
    a = (a[length:])
    for i in indices:
        a.insert(i, -1)
        
    
    return a