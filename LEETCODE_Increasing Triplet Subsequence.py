class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')
        middle = float('inf')

        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= middle:
                middle = num
            else:
                return True

        return False
