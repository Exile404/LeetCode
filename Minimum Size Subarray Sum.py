class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_length = float('inf')
        if sum(nums)<target:
            return 0
        summ = 0

        while right < len(nums):
            summ += nums[right]

            while summ >= target:
                min_length = min(min_length, right - left + 1)
                summ -= nums[left]
                left += 1

            right += 1

        
        return min_length
