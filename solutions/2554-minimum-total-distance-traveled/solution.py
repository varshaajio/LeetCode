class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort both to ensure the relative order is maintained for optimality
        robot.sort()
        factory.sort()
        
        n, m = len(robot), len(factory)
        
        # dp[i][j] represents the minimum distance to repair the first i robots 
        # using the first j factories.
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        
        # Base case: 0 robots require 0 distance, regardless of how many factories are available
        for j in range(m + 1):
            dp[0][j] = 0
            
        for j in range(1, m + 1):
            factory_pos, limit = factory[j-1]
            for i in range(n + 1):
                # Case 1: We don't use the current factory (j) for any robots.
                # It inherits the cost from using the previous j-1 factories for i robots.
                dp[i][j] = dp[i][j-1]
                
                # Case 2: We use the current factory to repair 'k' robots.
                # We pick the k robots closest to this factory from the remaining set (the rightmost ones).
                current_dist = 0
                for k in range(1, min(i, limit) + 1):
                    current_dist += abs(robot[i - k] - factory_pos)
                    
                    if dp[i - k][j - 1] != float('inf'):
                        dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + current_dist)
                        
        return dp[n][m]
