class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        m=-1
        n=len(s)
        for i in range(n):
            if s[i]==s[n-i-1]:
                return i
        return m
