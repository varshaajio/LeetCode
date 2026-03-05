class Solution:
    def minOperations(self, s: str) -> int:
        c0 = 0
        for i in range(len(s)):
            if i % 2:
                if s[i] != '0':
                    c0 += 1
            else:
                if s[i] != '1':
                    c0 += 1     
        return min(c0,len(s)-c0)
