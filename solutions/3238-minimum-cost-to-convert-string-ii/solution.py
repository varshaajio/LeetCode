from typing import List
import math

class TrieNode:
    def __init__(self):
        self.children = {}
        self.output = [] # Stores pairs of (length, string_id)

class Solution:
    def minimumCost(
        self, 
        source: str, 
        target: str, 
        original: List[str], 
        changed: List[str], 
        cost: List[int]
    ) -> int:
        n = len(source)
        
        # 1. Map unique strings to IDs for the graph
        unique_strs = list(set(original) | set(changed))
        str_to_id = {s: i for i, s in enumerate(unique_strs)}
        m = len(unique_strs)
        
        # 2. Floyd-Warshall for shortest transformation paths
        dist = [[math.inf] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
            
        for o, c, w in zip(original, changed, cost):
            u, v = str_to_id[o], str_to_id[c]
            dist[u][v] = min(dist[u][v], w)
            
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # 3. Build a Trie for the 'original' strings to match source[i:] quickly
        root = TrieNode()
        for s in unique_strs:
            node = root
            for char in s:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.output.append((len(s), str_to_id[s]))

        # 4. DP with Trie-based matching
        dp = [math.inf] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == math.inf:
                continue
            
            # Option 1: Characters match, no transformation needed
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            
            # Option 2: Transformation via Trie lookup
            # We look for all 'original' strings starting at source[i]
            # and check if they can transform into the substring at target[i]
            node = root
            for j in range(i, n):
                if source[j] not in node.children:
                    break
                node = node.children[source[j]]
                
                # Check all strings ending at this Trie node
                for length, u_id in node.output:
                    # Does the target match a potential transformation 'v'?
                    # We need target[i : i+length] to be some 'v' 
                    # such that dist[u_id][v_id] is finite.
                    target_sub = target[i : i + length]
                    if target_sub in str_to_id:
                        v_id = str_to_id[target_sub]
                        if dist[u_id][v_id] != math.inf:
                            dp[i + length] = min(dp[i + length], dp[i] + dist[u_id][v_id])
                            
        return dp[n] if dp[n] != math.inf else -1
