class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        lst = s.split()
        l = len(lst)
        st = ""
        for i in range(l-1,-1,-1):
            if(i==l-1):
                st = st+lst[i]
            else:
                st = st+" "+lst[i]
        return st