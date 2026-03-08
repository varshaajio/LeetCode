class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            current_char = nums[i][i]
            res.append("1" if current_char == "0" else "0")
        return "".join(res)
