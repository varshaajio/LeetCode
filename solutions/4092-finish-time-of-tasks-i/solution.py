class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        g=[]
        for i in range(n):
            g.append([])
        for k,l in edges:
            g[k].append(l)
        o=[]
        st=[0]
        while st:
            k=st.pop()
            o.append(k)
            for l in g[k]:
                st.append(l)
        f=n*[0]
        for k in reversed(o):
            if not g[k]:
                f[k]=baseTime[k]
            else:
                mn=float('inf')
                mx=0
                for l in g[k]:
                    mn=min(mn,f[l])
                    mx=max(mx,f[l])
                f[k]=mx+(mx-mn+baseTime[k])
        return f[0]
