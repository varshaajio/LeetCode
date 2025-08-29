class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        oddn = (n+1)// 2
        evenn = n//2

        oddm = (m+1) //2
        evenm = m//2

        return (oddn * evenm) +(evenn* oddm)

