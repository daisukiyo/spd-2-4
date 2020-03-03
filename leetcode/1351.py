# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

# Return the number of negative numbers in grid.

def countNegatives(self, grid: List[List[int]]) -> int:
    height = len(grid)
    width = len(grid[0])
    count = 0
    for i in range(height):
        for j in range(width): 
            if grid[i][j] < 0:
                count += 1
    return count