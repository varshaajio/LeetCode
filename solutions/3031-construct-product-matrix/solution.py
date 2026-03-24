class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        # Idea 1: Math : TLE - large number division

        n, m = len(grid), len(grid[0])

        MOD = 12345

        # allprod = 1

        # for i in range(n):
        #     for j in range(m):
        #         allprod *= grid[i][j]
        # # allprod = allprod % MOD
        # for i in range(n):
        #     for j in range(m):
        #         grid[i][j] = (allprod//grid[i][j]) % MOD // large integer division does not work
        
        #         Trick 2 : Use log
        #         diff = math.log2(allprod) - math.log2(grid[i][j])
        #         grid[i][j] = int(pow(2, diff)) % MOD
        
        # return grid

        # Idea 2: Flatten + Running Prefix + Suffix array

        suff = [1 for j in range(m*n)] # suff[i] -> product from index i+1 until the end of list

        arr = [] # stores the flattened grid
        for row in grid:
            arr += row

        # initialize suffix product
        p = 1
        for j in range(m*n-2, -1, -1):
            suff[j] = (arr[j+1]*suff[j+1]) % MOD
        
        # Iterate and populate prefix product        
        pref = 1
        for i, e in enumerate(arr):
            x, y = i//m, i%m # index for the 2D result matrix
            grid[x][y] = (pref*suff[i]) % MOD
            pref = (pref*arr[i]) % MOD

        return grid
