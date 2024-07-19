class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        l=len(nums)
        for i in range(l):
            for j in range(l):
                if(nums[i]+nums[j]==target and i!=j):
                    if(i in lst):
                        continue
                    else:
                        lst.append(i)
                    if(j in lst):
                        continue
                    else:
                        lst.append(j)
        return lst
        