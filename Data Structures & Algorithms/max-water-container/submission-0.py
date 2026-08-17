class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxh = (r - l) * min(heights[l], heights[r])

        while l < r:
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            current = (r - l) * min(heights[l], heights[r])
            maxh = max(maxh, current)

        return maxh