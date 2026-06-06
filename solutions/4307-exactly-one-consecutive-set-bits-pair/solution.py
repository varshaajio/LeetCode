class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        p=0
        while n>=1:
            if n&3==3:
                p+=1
            n>>=1
        return True if p==1 else False
