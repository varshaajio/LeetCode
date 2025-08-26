class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        ldiagsq=0
        for l,w in dimensions:
            if (l**2+w**2)>ldiagsq:
                ldiagsq=l**2+w**2
                area=l*w
            elif (l**2+w**2)== ldiagsq:
                area=max(area,l*w)       
        return area

