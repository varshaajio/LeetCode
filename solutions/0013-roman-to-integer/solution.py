class Solution:
    def romanToInt(self, s: str) -> int:
        symval={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        integer=0
        prev=0
        for i in range(len(s)-1,-1,-1):
            value=symval[s[i]]
            if value<prev:
                integer-=value
            else:
                integer+=value
            prev=value
        return integer

