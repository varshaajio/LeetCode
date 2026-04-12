class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a=sides[0]
        b=sides[1]
        c=sides[2]
        if a+b<=c or b+c<=a or a+c<=b:
            return []
        angA= math.acos((b**2+c**2-a**2)/(2*b*c))
        angB= math.acos((a**2+c**2-b**2)/(2*a*c))
        angC= math.acos((a**2+b**2-c**2)/(2*a*b))
        A=[0,0,0]
        A[0]=math.degrees(angA)
        A[1]=math.degrees(angB)
        A[2]=math.degrees(angC)
        A.sort()
        return A
        
