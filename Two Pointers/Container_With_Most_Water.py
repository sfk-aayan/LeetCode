class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
        