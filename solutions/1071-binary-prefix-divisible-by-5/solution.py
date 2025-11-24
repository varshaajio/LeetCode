class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        res = []
        rem = 0  # current value modulo 5
        for bit in nums:
            # shift left by 1 and add the new bit, then reduce modulo 5
            rem = (rem * 2 + bit) % 5
            res.append(rem == 0)
        return res

