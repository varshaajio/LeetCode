class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        max_dist = 0
        n1, n2 = len(nums1), len(nums2)
        
        # We iterate through both arrays using two pointers
        while i < n1 and j < n2:
            # Condition 1: i <= j
            # Condition 2: nums1[i] <= nums2[j]
            if nums1[i] <= nums2[j]:
                # If valid, update max_dist and try to increase j
                # to see if a larger distance exists for this i
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                # If nums1[i] > nums2[j], this i is too large.
                # Increment i to get a smaller value (non-increasing property)
                i += 1
                # Ensure j doesn't fall behind i to keep the distance calculation valid
                if j < i:
                    j = i
                    
        return max_dist
