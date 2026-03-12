class DisJointSet:
    def __init__(self, n):
        self.components = n
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def findPar(self, node: int) -> int:
        if node != self.parent[node]:
            self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]

    
    def unite(self, u, v):
        pu, pv = self.findPar(u), self.findPar(v)

        if pu == pv : return False

        if self.rank[pu] > self.rank[pv]:
            self.rank[pu] += 1
            self.parent[pv] = pu
        else:
            self.rank[pv] += 1
            self.parent[pu] = pv

        self.components -= 1
        return True

    def count(self):
        return self.components
    
        
class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        dsu = DisJointSet(n)

        edges.sort(key = lambda x : (-x[3], -x[2]))

        not_upgraded = (n - 1) - k
        ans = float("inf")

        for u, v, s, must in edges:
            if must:
                if not dsu.unite(u, v): return -1
                ans = min(ans, s)
                not_upgraded -= 1
            else:
                if not dsu.unite(u, v): continue
                if not_upgraded > 0:
                    ans = min(ans, s)
                    not_upgraded -= 1
                else:
                    ans = min(ans, 2 * s)
        
        return -1 if dsu.count() > 1 else ans
                
