class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=0
        for i in set(nums):
            c=nums.count(i)
            if c%k==0:
                s+=i*c
        return s
