class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        cols=len(grid[0]) if rows>0 else 0
        minr=rows
        minc=cols
        maxr=maxc=-1
        for r in range(rows):
            for c  in range(cols):
                if grid[r][c]==1:
                    minr=min(minr,r)
                    minc=min(minc,c)
                    maxr=max(maxr,r)
                    maxc=max(maxc,c)
        if maxr==-1:
            return 0
        h=maxr-minr+1
        w=maxc-minc+1
        return h*w
