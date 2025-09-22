class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        u=set(nums)
        m=max(nums.count(i) for i in u)
        return sum(nums.count(i) for i in u if nums.count(i)==m) 

