class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        cnt = 0
        for j in range(1, len(nums)):
            if nums[cnt] != nums[j]:
                cnt += 1
                nums[cnt] = nums[j]
        return cnt+1
