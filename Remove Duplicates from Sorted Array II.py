class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        count = 1  
        prev = nums[0]  
        k = 1 

        for i in range(1, len(nums)):
            if nums[i] == prev:
                count += 1
            else:
                count = 1
                prev = nums[i]

            if count <= 2:
                nums[k] = nums[i]
                k += 1

        return k
