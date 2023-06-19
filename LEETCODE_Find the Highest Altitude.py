class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        high_alt = 0
        for i in gain:
            altitude+=i
            high_alt = max(high_alt,altitude)
        return high_alt
