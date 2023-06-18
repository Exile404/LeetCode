class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left, right = 0, n-1
        maxLeft, maxRight = 0, 0
        water = [0] * n

        while left <= right:
            if height[left] <= height[right]:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    water[left] = maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    water[right] = maxRight - height[right]
                right -= 1

        return sum(water)
