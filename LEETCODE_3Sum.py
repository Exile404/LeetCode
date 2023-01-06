class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

    # initialize the result list
        result = []

        # iterate through the array
        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # set the target sum
            target = -nums[i]

            
            left = i + 1
            right = len(nums) - 1

            # use binary search to find the other two elements
            while left < right:
                # if the sum is equal to the target, add the triplet to the result list
                x = nums[left] + nums[right]
                if x == target:
                    result.append([nums[i], nums[left], nums[right]])
                    # skip duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    # move the pointers
                    left += 1
                    right -= 1
                # if the sum is less than the target, increment the left pointer
                elif x < target:
                    left += 1
                # if the sum is greater than the target, decrement the right pointer
                else:
                    right -= 1

        return result
