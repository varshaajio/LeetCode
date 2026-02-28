class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        flag=True
        while flag:
            flag=False
            i=0
            s1=set()
            for e in s:
                if e not in s1:
                    s1.add(e)
                else:
                    if i-s.rfind(e,0,i)<=k:
                        flag=True
                        s=s[:i]+s[i+1:]
                if flag==True:
                    break
                i+=1
        return s
