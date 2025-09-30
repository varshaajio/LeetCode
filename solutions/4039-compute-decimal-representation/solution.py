class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        s=str(n)
        n=len(s)-1
        lst=[]
        for i in s:
            if int(i)!=0:
                lst.append(int(i)*10**n)
            n-=1
        return lst
