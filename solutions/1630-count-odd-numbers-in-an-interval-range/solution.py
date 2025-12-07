class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c=ceil((high-low)/2)
        if low%2!=0 and high%2!=0:
            return c+1
        else:
            return c

