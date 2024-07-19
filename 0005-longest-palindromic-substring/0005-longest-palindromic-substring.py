class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        st = ""
        rev = ""
        l = len(s)
        for i in range(l):
            j = i
            while(j<l):
                st = st+s[j]
                rev = s[j]+rev
                if(rev==st):
                    leng = len(st)
                    d[st] = leng
                j+=1
            rev = ""
            st = ""
        high = 0
        for i in d:
            if(d[i]>high):
                high = d[i]
                ans = i
        return ans