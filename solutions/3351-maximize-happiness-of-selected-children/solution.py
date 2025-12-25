class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        t=0
        for i in range(k):
            c=happiness[i]-i
            if c>0:
                t+=c
            else:
                break
        return t
        
