class Solution:
    def splitArray(self, nums):
        n = len(nums)
        if n == 0:
            return -1  

        
        p = [nums[0]]
        for i in range(1, n):
            p.append(p[i - 1] + nums[i])

        
        incarr = [True]
        for i in range(1, n):
            if nums[i] > nums[i - 1] and incarr[i - 1]:
                incarr.append(True)
            else:
                incarr.append(False)

        
        decarr = [False] * n
        decarr[-1] = True  
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1] and decarr[i + 1]:
                decarr[i] = True

        
        ans = 10 ** 10
        found = False

        
        for i in range(n - 1):
            if incarr[i] and decarr[i + 1]:
                l = p[i]
                r = p[n - 1] - p[i]
                d = abs(l - r)
                if d < ans:
                    ans = d
                found = True

        
        return ans if found else -1

