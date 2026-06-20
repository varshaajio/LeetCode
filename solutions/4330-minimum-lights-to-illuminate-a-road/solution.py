class Solution:
    def minLights(self, lights: list[int]) -> int:
        d=(len(lights)+1)*[0]
        for i,j in enumerate(lights):
            if j>0:
                l=max(i-j,0)
                r=min(i+j,len(lights)-1)
                d[l]+=1
                d[r+1]-=1
        v=len(lights)*[False]
        c=0
        for i in range(len(lights)):
            c+=d[i]
            if c>0:
                v[i]=True
            else:
                v[i]=False
        a=0
        i=0
        while i<len(lights):
            if v[i]:
                i+=1
                continue
            ctr=min(len(lights)-1,i+1)
            cr=min(len(lights)-1,ctr+1)
            a+=1
            i=cr+1
        return a
