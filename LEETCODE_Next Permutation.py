class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums)-2
        while pivot >=0 and nums[pivot] >= nums[pivot+1]:
            pivot -=1
        if pivot < 0:
            nums.sort()
            return
        
        store = len(nums) - 1
        while nums[store] <= nums[pivot]:
            store -= 1
        nums[pivot],nums[store]=nums[store],nums[pivot]
        nums[pivot+1:] = nums[:pivot:-1]
