class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        from collections import defaultdict
        y_groups = defaultdict(int)
        
        for x, y in points:
            y_groups[y] += 1
        
        
        vals = []
        for cnt in y_groups.values():
            if cnt >= 2:
                vals.append(cnt * (cnt - 1) // 2)
        
        if len(vals) < 2:
            return 0
        
        total_sum = sum(vals) % MOD
        sum_sq = sum((v * v) % MOD for v in vals) % MOD
        
        
        ans = (total_sum * total_sum - sum_sq) % MOD
        ans = ans * pow(2, MOD-2, MOD) % MOD  
        
        return ans

