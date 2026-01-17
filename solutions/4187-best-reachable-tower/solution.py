class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        cx=center[0]
        cy=center[1]
        tq=-1
        tc=[-1,-1]
        for a in towers:
            x=a[0]
            y=a[1]
            q=a[2]
            d=abs(x-cx)+abs(y-cy)
            if d<=radius and (q>tq or (q==tq and [x,y]<tc)):
                tq=q
                tc=[x,y]
        return tc
