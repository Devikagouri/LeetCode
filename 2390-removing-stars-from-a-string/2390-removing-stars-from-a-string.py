class Solution(object):
    def __init__(self):
        self.stack = []
        self.top = -1
    def push(self,ch):
        self.top+=1
        self.stack.append(ch)
        
    def pop(self):
        self.stack.pop(self.top)
        self.top-=1
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in s:
            if(i!='*'):
                self.push(i)
            else:
                self.pop()
        st = ''
        for i in self.stack:
            st = st+str(i)
        return st