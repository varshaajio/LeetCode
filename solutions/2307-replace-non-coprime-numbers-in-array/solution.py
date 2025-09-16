class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        while(i<len(nums)-1):
            p,q=nums[i],nums[i+1]
            while(q>0):
                p,q=q,p%q
            if(p>1):
                nums[i]=(nums[i]*nums[i+1])//p
                nums.pop(i+1)
                if i>0:
                    i-=1
            else:
                i+=1
        return nums

        
