class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lst = []
        for i in nums:
            if(i!=val):
                lst.append(i)
        l = len(lst)
        for i in range(l):
            nums[i] = lst[i]
        return(l)

              