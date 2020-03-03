# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    for i in range(len(A)):
        # reverses each list in-place (overwrites)
        A[i].reverse()
        # invert the value of every list
        for j in range(len(A[i])):
            if A[i][j] == 1:
                A[i][j] = 0
            else:
                A[i][j] = 1
    return A