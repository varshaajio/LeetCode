class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        startRow, endRow = x, x + k - 1
        
        while startRow < endRow:
            for j in range(y, y + k):
                grid[startRow][j], grid[endRow][j] = grid[endRow][j], grid[startRow][j]
            
            startRow += 1
            endRow -= 1
        
        return grid
