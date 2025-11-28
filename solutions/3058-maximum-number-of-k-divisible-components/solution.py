class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(10**6)

        # build adjacency list
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        # keep values modulo k to avoid huge sums
        vals_mod = [v % k for v in values]

        cuts = [0]  # use list to mutate inside nested function

        def dfs(u, p):
            subtotal = vals_mod[u]
            for v in g[u]:
                if v == p:
                    continue
                child_mod = dfs(v, u)
                if child_mod == 0:
                    # can cut the edge u-v; child becomes its own component
                    cuts[0] += 1
                else:
                    subtotal = (subtotal + child_mod) % k
            return subtotal

        dfs(0, -1)  # root anywhere; total sum is divisible by k per constraints
        return cuts[0] + 1

