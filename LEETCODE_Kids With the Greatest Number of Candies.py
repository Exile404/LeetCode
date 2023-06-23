class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        l = []
        for i in candies:
            if i+extraCandies>=max_num:
                l.append(True)
            else:
                l.append(False)
        return l
