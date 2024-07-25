class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1 = len(str1)
        l2 = len(str2)
        if(l1>l2):
            low = str2
            high = str1
            h = l1
            l = l2
        else:
            low = str1
            high = str2
            h = l2
            l = l1
        
        st = ''
        for i in range(h):
            j = 1
            st = low[0:(l-i)]
            s = ''
            while(len(s)<=h and st!=''):                
                s = st*j
                print(st)
                if(s==high):
                    k = 1
                    while(k<=l):
                        if((st*k)==low):
                            return st
                        k+=1
                print(i,j)
                j+=1
        return ''