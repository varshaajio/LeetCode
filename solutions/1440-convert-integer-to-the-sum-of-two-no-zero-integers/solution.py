class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        i=1
        while i<=n//2:
            j=n-i
            if not '0' in str(i)+str(j):
                return [i,j]
            i+=1
