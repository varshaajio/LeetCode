class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=len(nums)
        ls=0
        rs=sum(nums)-nums[0]
        out=[abs(ls-rs)]
        for i in range(l-1):
            ls+=nums[i]
            rs-=nums[i+1]
            out.append(abs(ls-rs))
        return out
