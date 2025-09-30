class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
       """
        n = len(nums)
        r = 0
        c = 1

        for i in range(n):
            r=(r+c*nums[i]) % 10
            if i<(n-1):
                c=c*(n-1-i) // (i+1)
        
        return r
