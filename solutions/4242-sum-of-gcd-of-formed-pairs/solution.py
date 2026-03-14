from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        p=[]
        m=0
        for i in nums:
            m=max(i,m)
            p.append(gcd(i,m))
        p.sort()
        l,s=0,0
        r=len(p)-1
        while l<r:
            s+=gcd(p[l],p[r])
            l+=1
            r-=1
        return s
