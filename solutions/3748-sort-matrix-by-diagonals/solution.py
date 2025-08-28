class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if i == 0 or j == 0:  
                    diag = []
                    x, y = i, j
                    while x < n and y < n:
                        diag.append(grid[x][y])
                        x += 1; y += 1
                    if i >= j:  
                        diag.sort(reverse=True)   
                    else:
                        diag.sort()
                    x, y = i, j
                    for v in diag:
                        grid[x][y] = v
                        x += 1; y += 1

        return grid

