class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        g=[]
        for i in range(m):
            g.append(n*['#'])
        for x in range(n):
            g[0][x]="."
        for y in range(m):
            g[y][n-1]="."
        o=[]
        for r in g:
            o.append(''.join(r))
        return o
            
