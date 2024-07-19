class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        st = ""
        leng = len(s)
        print(leng)
        for j in range(leng):
            i = j
            while(i<leng):
                if(s[i] not in st):
                        st = st+s[i]
                        if(i+1==leng):
                            l = len(st)
                            print(st,l)
                            d[st] = l
                            st = ""
                            break
                    
                else:
                    l = len(st)
                    print(st,l)
                    d[st] = l
                    st = ""
                    break
                i+=1
        high = 0
        for i in d:
            if(d[i]>high):
                high = d[i]              
        return high