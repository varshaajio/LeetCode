class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        # We use two arrays to optimize space: 
        # prev_dp stores max profit for (t-1) transactions
        # curr_dp stores max profit for (t) transactions
        prev_dp = [0] * n
        curr_dp = [0] * n
        
        # Iterate for each allowed transaction from 1 to k
        for t in range(k):
            # max_diff_normal tracks: max(prev_dp[p-1] - prices[p])
            # max_diff_short tracks:  max(prev_dp[p-1] + prices[p])
            # Initialize for the hypothetical start at day p=0
            max_diff_normal = -prices[0]
            max_diff_short = prices[0]
            
            curr_dp[0] = 0 # Cannot complete a transaction on the first day
            
            for i in range(1, n):
                # Option 1: Don't transact on day i (carry forward previous day's best)
                profit_rest = curr_dp[i-1]
                
                # Option 2: Complete a Normal transaction (Buy earlier, Sell now at i)
                profit_normal = prices[i] + max_diff_normal
                
                # Option 3: Complete a Short transaction (Short earlier, Buy back now at i)
                profit_short = -prices[i] + max_diff_short
                
                # Take the best option
                curr_dp[i] = max(profit_rest, profit_normal, profit_short)
                
                # Update the running max diffs for the next day's calculation
                # We consider day 'i' as a potential start day for a future transaction.
                # The profit before starting at 'i' must come from 'prev_dp[i-1]' 
                # to ensure non-overlapping intervals.
                prev_profit_base = prev_dp[i-1]
                
                max_diff_normal = max(max_diff_normal, prev_profit_base - prices[i])
                max_diff_short = max(max_diff_short, prev_profit_base + prices[i])
            
            # Update prev_dp to be the current round for the next iteration
            prev_dp = list(curr_dp)
            
        return prev_dp[-1]
