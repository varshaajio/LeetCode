class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        cur = 0   # current consecutive '1's length
        ans = 0
        for ch in s:
            if ch == '1':
                cur += 1
                ans = (ans + cur) % MOD
            else:
                cur = 0
        return ans

