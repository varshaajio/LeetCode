class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        pair=[-1,-1]
        f={}
        for i in nums:
            if i not in f:
                f[i]=1
            else:
                f[i]+=1
        u=f.keys()
        s=sorted(u)
        for i in range(len(s)-1):
            a=s[i]
            for j in range(i+1,len(s)):
                b=s[j]
                if f[a]!=f[b]:
                    pair[0]=a
                    pair[1]=b
                    return pair
        return pair
