# Below we will define an n-interesting polygon.
# Your task is to find the area of a polygon for a given n.

def shapeArea(n):
    #1, 5, 13, 25
    #1, 2(4+1), 3(9+4), 4(16+9)
    if n == 1:
        return 1
    else:
        return (n**2 + (n-1)**2)
