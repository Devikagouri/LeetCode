class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if(x<0):
            flag = True
            x = -x
        rev = 0
        while(x>0):
            r = x%10
            rev = rev*10+r
            x = x//10
        if(rev>((2**31)-1) or rev<-2**31):
            return 0
        elif(flag==True):
            return -rev
        else:
            return rev