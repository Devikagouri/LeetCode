class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        i = x
        rev=0
        while(i>0):
            r = i%10
            rev=rev*10+r
            i = i//10
        if(rev==x):
            return True
        else:
            return False