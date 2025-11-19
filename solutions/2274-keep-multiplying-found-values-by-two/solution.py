class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        s = set(nums)
        while original in s:
            original *= 2
        return original

