class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = []
        st = ''
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            if(i in vowel):
                lst.append(i)
        l = len(lst)-1
        for i in s:
            if(i in vowel):
                st = st+lst[l]
                l = l-1
            else:
                st = st+i
        return st