import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        # adj[u] stores (v, weight) for normal edges u -> v
        adj = defaultdict(list)
        # rev_adj[u] stores (v, weight) for incoming edges v -> u
        # which can be reversed to u -> v
        rev_adj = defaultdict(list)
        
        for u, v, w in edges:
            adj[u].append((v, w))
            rev_adj[v].append((u, w))
            
        # min_cost[i] will store the minimum cost to reach node i
        min_cost = [float('inf')] * n
        min_cost[0] = 0
        
        # Priority queue stores (cost, current_node)
        pq = [(0, 0)]
        
        while pq:
            curr_dist, u = heapq.heappop(pq)
            
            if curr_dist > min_cost[u]:
                continue
            
            if u == n - 1:
                return curr_dist
            
            # 1. Try normal outgoing edges
            for v, w in adj[u]:
                if curr_dist + w < min_cost[v]:
                    min_cost[v] = curr_dist + w
                    heapq.heappush(pq, (min_cost[v], v))
            
            # 2. Try reversing an incoming edge (u's switch)
            # The rule: "when you arrive at ui... you may activate it... reverse that edge"
            for v, w in rev_adj[u]:
                reversed_cost = curr_dist + (2 * w)
                if reversed_cost < min_cost[v]:
                    min_cost[v] = reversed_cost
                    heapq.heappush(pq, (min_cost[v], v))
                    
        return min_cost[n-1] if min_cost[n-1] != float('inf') else -1
