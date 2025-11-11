class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        counts = [(s.count('0'), len(s) - s.count('0')) for s in strs]

        for z, o in counts:
            if z > m or o > n:
                continue
            for i in range(m, z - 1, -1):
                row = dp[i]
                prev = dp[i - z]
                for j in range(n, o - 1, -1):
                    val = prev[j - o] + 1
                    if val > row[j]:
                        row[j] = val
        return dp[m][n]

