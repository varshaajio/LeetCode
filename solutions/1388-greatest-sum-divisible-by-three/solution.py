class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[r] = max sum with remainder r (mod 3)
        NEG_INF = float('-inf')
        dp = [0, NEG_INF, NEG_INF]

        for num in nums:
            new_dp = dp[:]  # copy current bests
            for r in range(3):
                if dp[r] != NEG_INF:
                    s = dp[r] + num
                    new_dp[s % 3] = max(new_dp[s % 3], s)
            dp = new_dp

        return dp[0]

