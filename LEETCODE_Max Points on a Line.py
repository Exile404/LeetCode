
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_points = 0
        n = len(points)
        for i in range(n):
            grab_point = points[i]
            slope_c = {}
            duplicate_point = 1
            for j in range(i+1,n):
                com_point = points[j]
                if grab_point == com_point:
                    duplicate_point+=1
                else:
                    try:
                        slope = (com_point[1]-grab_point[1])/(com_point[0]-grab_point[0])
                    except:
                        slope = 'inf'
                    if slope not in slope_c:
                        slope_c[slope] = 1
                    else:
                        slope_c[slope] += 1
            max_points = max(max_points,duplicate_point)
            for (slope,count) in slope_c.items():
                max_points = max(max_points,duplicate_point + count)
        return max_points
