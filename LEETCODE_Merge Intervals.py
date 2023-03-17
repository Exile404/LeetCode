class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        track_inv = intervals[0]
        for track in intervals[1:]:
            if track[0] <= track_inv[1]:
                track_inv[1] = max(track[1],track_inv[1])
            else:
                res.append(track_inv)
                track_inv = track
        res.append(track_inv)
        return res
