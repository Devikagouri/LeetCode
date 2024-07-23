class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        l = len(candies)
        lst = []
        count = 0
        for i in range(l):
            x = candies[i]
            y = x+extraCandies
            for j in range(l):
                if(i!=j and y<candies[j]):
                    count = 1
                    break
            if(count==1):
                lst.append(False)
                print(lst)
            else:
                lst.append(True)
                print(lst)
            count = 0
        return lst