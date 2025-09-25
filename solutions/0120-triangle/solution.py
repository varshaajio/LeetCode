class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        
        # Initialize dp with the last row of the triangle
        dp = triangle[-1][:]
        
        # Start from the second last row and move upwards
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Update dp[j] as the minimum path sum from this element to the bottom
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        
        # dp[0] will contain the minimum path sum from top to bottom
        return dp[0]

