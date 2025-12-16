import sys

# Increase recursion depth to handle deep hierarchies (up to N=160)
sys.setrecursionlimit(2000)

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # Build Adjacency List
        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)
        
        # Preprocess prices and profits (1-based index adjustment)
        # We store them in 1-based arrays for easier access with node ID u
        p = [0] * (n + 1)
        f = [0] * (n + 1)
        for i in range(n):
            p[i+1] = present[i]
            f[i+1] = future[i]

        # Helper function to merge two knapsack arrays
        # dp_target: The running total array
        # dp_source: The child's array to merge in
        # limit_target: The max index in dp_target that is not -inf
        # limit_source: The max index in dp_source that is not -inf
        def merge(dp_target, dp_source, limit_target, limit_source):
            # The new max weight we can form is the sum of the max weights of both, bounded by budget
            new_limit = min(budget, limit_target + limit_source)
            new_dp = [-float('inf')] * (budget + 1)
            
            # Optimization: Only iterate over valid ranges
            # We want to calculate new_dp[w + k] = dp_target[w] + dp_source[k]
            for k in range(limit_source + 1):
                val_k = dp_source[k]
                if val_k == -float('inf'): continue
                
                # For each valid item in source, add to all valid items in target
                # Check bounds to ensure we don't exceed budget
                max_w = min(limit_target, budget - k)
                
                for w in range(max_w + 1):
                    val_w = dp_target[w]
                    if val_w == -float('inf'): continue
                    
                    total_w = w + k
                    if val_w + val_k > new_dp[total_w]:
                        new_dp[total_w] = val_w + val_k
            
            return new_dp, new_limit

        def dfs(u):
            # Base accumulators for children results
            # agg_buy: Combined profit of children if u BUYS
            # agg_skip: Combined profit of children if u SKIPS
            
            # Initialize with 0 cost = 0 profit
            agg_buy = [-float('inf')] * (budget + 1)
            agg_buy[0] = 0
            limit_buy = 0
            
            agg_skip = [-float('inf')] * (budget + 1)
            agg_skip[0] = 0
            limit_skip = 0
            
            # 1. Merge all children into the accumulators
            for v in adj[u]:
                res_v_bought, res_v_not_bought = dfs(v)
                
                # Find the effective size of the returned arrays (optimization)
                # Scanning backwards to find the last valid entry
                limit_v_bought = 0
                for i in range(budget, -1, -1):
                    if res_v_bought[i] > -float('inf'):
                        limit_v_bought = i
                        break
                        
                limit_v_skip = 0
                for i in range(budget, -1, -1):
                    if res_v_not_bought[i] > -float('inf'):
                        limit_v_skip = i
                        break
                
                # If u buys, v sees "boss bought" -> merge res_v_bought
                agg_buy, limit_buy = merge(agg_buy, res_v_bought, limit_buy, limit_v_bought)
                # If u skips, v sees "boss not bought" -> merge res_v_not_bought
                agg_skip, limit_skip = merge(agg_skip, res_v_not_bought, limit_skip, limit_v_skip)
            
            # 2. Calculate final DP tables for u
            cost_full = p[u]
            prof_full = f[u] - cost_full
            
            cost_disc = p[u] // 2
            prof_disc = f[u] - cost_disc
            
            # Initialize results
            res_boss_bought = [-float('inf')] * (budget + 1)
            res_boss_not_bought = [-float('inf')] * (budget + 1)
            
            # --- Construct res_boss_bought (Boss of u bought) ---
            # Choice 1: u Skips. Profit comes from agg_skip.
            for w in range(limit_skip + 1):
                res_boss_bought[w] = agg_skip[w]
                
            # Choice 2: u Buys (Discounted). Profit comes from agg_buy + u's profit.
            for w in range(limit_buy + 1):
                if agg_buy[w] == -float('inf'): continue
                if w + cost_disc <= budget:
                    # Take max of current value (skip) vs new value (buy)
                    if agg_buy[w] + prof_disc > res_boss_bought[w + cost_disc]:
                        res_boss_bought[w + cost_disc] = agg_buy[w] + prof_disc
            
            # --- Construct res_boss_not_bought (Boss of u didn't buy) ---
            # Choice 1: u Skips. Profit comes from agg_skip.
            for w in range(limit_skip + 1):
                res_boss_not_bought[w] = agg_skip[w]
            
            # Choice 2: u Buys (Full Price). Profit comes from agg_buy + u's profit.
            for w in range(limit_buy + 1):
                if agg_buy[w] == -float('inf'): continue
                if w + cost_full <= budget:
                    if agg_buy[w] + prof_full > res_boss_not_bought[w + cost_full]:
                        res_boss_not_bought[w + cost_full] = agg_buy[w] + prof_full
                    
            return res_boss_bought, res_boss_not_bought

        # Employee 1 is the CEO (no boss), so we look at the "boss not bought" case
        _, final_res = dfs(1)
        
        # The answer is the max profit achievable within the budget
        ans = 0
        for x in final_res:
            if x > ans:
                ans = x
        return ans
