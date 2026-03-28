class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        m=-1
        n=-1
        t=len(nums)
        for i in range(t):
            if nums[i]==1:
                m=i
                if n!=-1:
                    t=min(t,abs(m-n))
            elif nums[i]==2:
                n=i
                if m!=-1:
                    t=min(t,abs(n-m))
        return t if t!=len(nums) else -1
