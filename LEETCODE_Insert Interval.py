class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        start, end = newInterval

        for x,y in intervals:
            # Checking that interval start before or not
            if y < start:
                result.append([x,y])
            elif x > end:
                result.append([start, end])
                start, end = x, y
            else:
                start = min(start, x)
                end = max(end, y)

        result.append([start, end])
        return result
