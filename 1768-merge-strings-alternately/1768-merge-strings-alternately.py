class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        lst1 = []
        lst2 = []
        lst = []
        for i in word1:
            lst1.append(i)
        for i in word2:
            lst2.append(i)
        l1 = len(lst1)
        l2 = len(lst2)
        if(l1>l2):
            l = l1
        else:
            l = l2
        for i in range(l):
            if(i<l1 and i<l2):
                lst.append(lst1[i])
                lst.append(lst2[i])
            elif(i<l1 and i==l2):
                for j in range(i,l1):
                    lst.append(lst1[j])
                break
            elif(i==l1 and i<l2):
                for j in range(i,l2):
                    lst.append(lst2[j])
                break
        s = ""
        for i in lst:
            s = s+i
        return s
            