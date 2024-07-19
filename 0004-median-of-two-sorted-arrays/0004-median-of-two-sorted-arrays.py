class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1+nums2
        nums3 = sorted(nums)
        l = len(nums3)
        if(l%2==0):
            mid = int(l/2)
            s = float(nums3[mid]+nums3[mid-1])
            median = s/2
        else:
            mid = int(math.ceil(l/2))
            median = nums3[mid]
        return median
        