class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numberofitems=len(nums)
        if numberofitems<3:
            return numberofitems
        m=2
        c=2
        for i in range(2,numberofitems):
            if nums[i]==(nums[i-1]+nums[i-2]):
                c+=1
            else:
                c=2
            if m<c:
                m=c
        return m
