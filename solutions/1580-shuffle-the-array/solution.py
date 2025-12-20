class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        for i in range(n):
            a.extend([nums[0+i],nums[n+i]])
        return a
