class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window_sum = sum(nums[:k])
        max_average = window_sum / k

        for i in range(k, n):
            window_sum += nums[i] - nums[i - k]
            max_average = max(max_average, window_sum / k)

        return max_average
