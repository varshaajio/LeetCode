class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # min prefix-sum seen for each remainder mod k
        min_pref = [float('inf')] * k
        # prefix sum at index 0 (no elements) has remainder 0
        min_pref[0] = 0
        
        pref = 0
        ans = -10**30  # sufficiently small sentinel (nums can be -1e9)
        
        for j in range(1, n+1):
            pref += nums[j-1]
            r = j % k
            # candidate: subarray ending at j whose length is divisible by k
            if min_pref[r] != float('inf'):
                ans = max(ans, pref - min_pref[r])
            # update minimum prefix for this remainder
            if pref < min_pref[r]:
                min_pref[r] = pref
        
        return ans

