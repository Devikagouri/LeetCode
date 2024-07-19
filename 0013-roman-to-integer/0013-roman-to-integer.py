class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = []
        l = 0
        check=0
        ans = 0
        for i in s:
            lst.append(i)
            l = l+1
        for i in range(l):
            if(check==1):
                check=0
                continue
            c = lst[i]
            if(i+1==l):
                d = 'Z'
            else:
                d = lst[i+1]

            if(c=='I'):
                if(d=='V'):
                    ans = ans+4
                    check=1
                elif(d=='X'):
                    ans = ans+9
                    check=1
                else:
                    ans = ans+1
                
            elif(c=='V'):
                ans = ans+5

            elif(c=='X'):
                if(d=='L'):
                    ans = ans+40
                    check=1
                elif(d=='C'):
                    ans = ans+90
                    check=1
                else:
                    ans = ans+10

            elif(c=='L'):
                ans = ans+50

            elif(c=='C'):
                if(d=='D'):
                    ans = ans+400
                    check=1
                elif(d=='M'):
                    ans = ans+900
                    check=1
                else:
                    ans = ans+100

            elif(c=='D'):
                ans = ans+500

            elif(c=='M'):
                ans = ans+1000
        return ans
        