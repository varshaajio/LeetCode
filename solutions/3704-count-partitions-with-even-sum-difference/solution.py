class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        p=0
        for i in range (1,len(nums)):
            if (sum(nums[0:i])-sum(nums[i:len(nums)]))%2==0:
                p+=1
        return p
