class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        p = 0
        for i in nums:
            l = l+1
        for i in range(l):
            if(nums[i]==target):
                return i
            else:
                if(nums[i]>target):
                    p=i
                    return p
                    
                elif(i==l-1):
                    p=l
                    return p
                
         
        