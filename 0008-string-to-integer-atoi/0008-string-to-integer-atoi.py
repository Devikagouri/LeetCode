class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        flag = False
        st = str(s.strip(" "))
        print(st,type(st))
        num = 0
        
        if(st.startswith('-')):
            flag = True
            st = st[1:l]
        elif(st.startswith('+')):
            st = st[1:l]
        for i in st:
            if(not(i>='0' and i<='9')):
                break
            n = int(i)
            num = num*10+n
            print(num)
        if(flag==True):
            num = -num
        if(num>((2**31)-1)):
            return (2**31)-1
        elif(num<(-(2**31))):
            return -(2**31)
        
        return num