class Solution:
    def residuePrefixes(self, s: str) -> int:
        s1=''
        c=0
        for i in range(len(s)):
            s1+=s[i]
            if len(set(s1))==len(s1)%3:
                c+=1
        return c
