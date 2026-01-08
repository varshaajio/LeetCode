class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        # Initialize DP table with negative infinity
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Current product of the elements at these indices
                curr_prod = nums1[i-1] * nums2[j-1]
            
                dp[i][j] = max(
                    curr_prod,                             # Start fresh with only current pair
                    curr_prod + dp[i-1][j-1],             # Add current pair to previous optimal
                    dp[i-1][j],                            # Skip nums1[i-1]
                    dp[i][j-1]                             # Skip nums2[j-1]
                )
                
        return dp[n][m]
