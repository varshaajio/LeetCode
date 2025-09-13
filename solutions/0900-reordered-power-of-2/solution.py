class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numsortlst=sorted(str(n))
    
        p=1
        while p<=10**9:
            if numsortlst==sorted(str(p)):
                return True
            p=p*2
        return False

        
