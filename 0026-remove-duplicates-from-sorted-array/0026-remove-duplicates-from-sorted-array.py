class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = []
        for i in nums:
            if(i not in lst):
                lst.append(i)
        l = len(lst)
        for i in range(l):
            nums[i] = lst[i]
        return l