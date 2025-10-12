class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        o = 0
        for i in range(n):
            freq = {}
            for j in range(i, n):
                c = s[j]
                freq[c] = freq.get(c, 0) + 1
                if len(freq) > 1:
                    vals = list(freq.values())
                    if max(vals) == min(vals):
                        o = max(o, j - i + 1)
                else:
                    # only one unique char so far
                    o = max(o, j - i + 1)
        return o

