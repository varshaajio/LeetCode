class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c=Counter(text)
        required={'b':1,'a':1,'l':2,'o':2,'n':1}.items()
        small=10**4+1
        for k,v in required:
            p=c[k]//v
            if small>p:
                small=p
        return small
