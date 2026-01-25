class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        c=[]
        nums.sort()
        for i in range(0,len(nums)-k+1):
                c.append(abs(nums[i+k-1]-nums[i]))
        if len(c)==0:
            return 0
        else:
            return min(c)
