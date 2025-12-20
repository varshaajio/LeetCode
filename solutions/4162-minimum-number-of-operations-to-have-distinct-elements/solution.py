class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        f={}
        d=0
        for b in nums:
            if b in f:
                if f[b]==1:
                    d+=1
                f[b]=f[b]+1
            else:
                f[b]=1
        n=0
        x=0
        l=len(nums)
        while x<l and d>0:
            m=min(x+3,l)
            for k in range(x,m):
                v=nums[k]
                if f[v]==2:
                    d-=1
                f[v]=f[v]-1
                if not f[v]:
                    del f[nums[k]]
            n+=1
            x=x+3
        return n
