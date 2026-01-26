class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 1000000
        result = []

        # Find minimum difference
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            min_diff = min(min_diff, diff)
            if min_diff==1:
                break

        # Collect pairs with minimum difference
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result   
