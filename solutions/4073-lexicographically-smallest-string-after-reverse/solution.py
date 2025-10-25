class Solution(object):
    def lexSmallest(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        c=[]
        for k in range(1,n+1):
            fkr=s[:k][::-1]+s[k:]
            c.append(fkr)

            lkr=s[:n-k]+s[n-k:][::-1]
            c.append(lkr)
        return min(c)
