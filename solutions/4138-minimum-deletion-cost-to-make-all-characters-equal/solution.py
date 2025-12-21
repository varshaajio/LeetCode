class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        t=sum(cost)
        k=26*[0] #for 26 alpha
        for i in range(len(s)):
            i1=ord(s[i])-97
            k[i1]=k[i1]+cost[i]
        m=max(k)
        return t-m
