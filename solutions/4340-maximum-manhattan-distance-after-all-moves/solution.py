class Solution:
    def maxDistance(self, moves: str) -> int:
        u=d=r=k=l=0
        for c in moves:
            if c=="U":
                u+=1
            elif c=="D":
                d+=1
            elif c=="R":
                r+=1
            elif c=="L":
                l+=1
            else:
                k+=1
        a=r-l
        b=u-d
        return abs(a)+abs(b)+k
