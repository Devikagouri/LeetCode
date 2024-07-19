class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        dd = float(dividend)
        ds = float(divisor)
        ans = dd/ds
        f_ans = math.trunc(ans)
        if(f_ans>((2**31)-1)):
            return ((2**31)-1)
        elif(f_ans<(-(2**31))):
            return (-(2**31))
        else:
            return f_ans