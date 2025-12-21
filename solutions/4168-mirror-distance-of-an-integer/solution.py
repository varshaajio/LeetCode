class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n):
            rem=0
            while n>=1:
                rem=rem*10+n%10
                n=n//10
            return rem
        return abs(n-reverse(n))
