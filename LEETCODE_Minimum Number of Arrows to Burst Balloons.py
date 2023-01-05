import math
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        pos = -math.inf
        point = 0
        for i,j in points:
            if i>pos:
                pos = j
                point+=1
            else:
                pos = min(pos,j)
        return point
        
