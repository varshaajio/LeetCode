class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        s=sorted(arr)
        n=s[1]-s[0]
        for i in range(2,len(arr)):
            if s[i]-s[i-1]!=n:
                return False
        return True
