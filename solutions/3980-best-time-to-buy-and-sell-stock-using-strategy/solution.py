class Solution(object):
    def maxProfit(self, prices, strategy, k):
        """
        :type prices: List[int]
        :type strategy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)

        # Step 1: Original profit
        base_profit = sum(strategy[i] * prices[i] for i in range(n))

        # Step 2: Precompute values for quick delta calculation
        # For first half → new = 0 → contribution = -old*price
        loss = [-(strategy[i] * prices[i]) for i in range(n)]
        # For second half → new = 1 → contribution = (1 - old)*price
        gain = [(1 - strategy[i]) * prices[i] for i in range(n)]

        # Prefix sums for O(1) window queries
        prefix_loss = [0] * (n + 1)
        prefix_gain = [0] * (n + 1)
        for i in range(n):
            prefix_loss[i+1] = prefix_loss[i] + loss[i]
            prefix_gain[i+1] = prefix_gain[i] + gain[i]

        # Step 3: Try all windows
        half = k // 2
        best_delta = 0
        for l in range(n - k + 1):
            r = l + k
            mid = l + half

            # sum over first half (loss), sum over second half (gain)
            delta = (prefix_loss[mid] - prefix_loss[l]) + (prefix_gain[r] - prefix_gain[mid])

            best_delta = max(best_delta, delta)

        # Step 4: Final answer
        return base_profit + best_delta

