class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = n
        shift = n >> 1
        while shift:
            res ^= shift
            shift >>= 1
        return res

