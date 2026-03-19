class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        count = 0

        rows, cols = len(grid), len(grid[0])

        grid_new = [[0] * cols for i in range(rows)]
        grid_x = [[0] * cols for i in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "X":
                    grid_new[row][col] = 1
                    grid_x[row][col] = 1
                elif grid[row][col] == "Y":
                    grid_new[row][col] = -1
        
        for col in range(cols):
            for row in range(rows):
                prev = grid_new[row - 1][col] if row > 0 else 0
                grid_new[row][col] += prev

                prev_x = grid_x[row - 1][col] if row > 0 else 0
                grid_x[row][col] += prev_x

        for row in range(rows):
            for col in range(cols):         
                prev = grid_new[row][col - 1] if col > 0 else 0
                prev_x = grid_x[row][col - 1] if col > 0 else 0
                grid_x[row][col] += prev_x
                grid_new[row][col] += prev 

                if grid_x[row][col] > 0 and grid_new[row][col] == 0:
                    count += 1

        return count
