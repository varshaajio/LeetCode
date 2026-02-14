class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        c=0
        d={}
        for w in words:
            if k<=len(w):
                p=w[:k]
                if p in d:
                    d[p]+=1
                else:
                    d[p]=1
        for k in d:
            if 2<=d[k]:
                c=c+1
        return c
