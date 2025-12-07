class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def rev(a):
            revbin=int(bin(a)[2:][::-1],2)
            return revbin
        def rec(n):
            return (rev(n),n)
        s=sorted(nums,key=rec)
        return s
