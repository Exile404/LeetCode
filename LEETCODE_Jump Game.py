class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        n = len(nums)
        for i in range(n):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])
            if max_index >= n - 1:
                return True
        return False
