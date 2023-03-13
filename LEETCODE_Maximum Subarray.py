class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import math
        max_index = 0
        maxx= -math.inf
        for i in range(len(nums)):
            max_index = max(nums[i], max_index + nums[i])
            maxx = max(maxx, max_index)
        return maxx
