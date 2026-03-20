class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows, cols = m - k + 1, n - k + 1
        ans = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                vals = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.add(grid[x][y])
                if len(vals) == 1:
                    ans[i][j] = 0
                else:
                    sorted_vals = sorted(vals)
                    min_diff = min(sorted_vals[p] - sorted_vals[p-1] for p in range(1, len(sorted_vals)))
                    ans[i][j] = min_diff
        return ans
