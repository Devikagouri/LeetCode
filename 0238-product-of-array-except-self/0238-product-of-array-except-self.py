import numpy as np
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        p1 = []
        p2 = []
        lst = []
        p = 1
        p1.append(1)
        p2.append(1)
        for i in range(1,l):
            print(nums[i-1])
            p = p*nums[i-1]
            p1.append(p)
        print(p1)
        r_nums = nums[::-1]
        p = 1
        for i in range(1,l):
            p = p*r_nums[i-1]
            p2.append(p)
        print(p2)
        r_p2=p2[::-1]
        for i in range(l):
            s = p1[i]*r_p2[i]
            lst.append(s)
        return(lst)  