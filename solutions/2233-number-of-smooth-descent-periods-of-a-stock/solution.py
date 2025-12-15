class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = 0
        streak = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                streak += 1
            else:
                total += streak * (streak + 1) // 2
                streak = 1

        
        total += streak * (streak + 1) // 2
        return total

