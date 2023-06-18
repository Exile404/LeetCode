import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = math.inf
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if abs(summ - target) < abs(res - target):
                    res = summ
                if summ < target:
                    left += 1
                elif summ > target:
                    right -= 1
                else:
                    return res
        return res
