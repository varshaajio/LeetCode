class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        zeros = k
        
        for x in nums:
            if x == 1:
                if zeros < k:
                    return False
                zeros = 0
            else:
                zeros += 1
        
        return True
