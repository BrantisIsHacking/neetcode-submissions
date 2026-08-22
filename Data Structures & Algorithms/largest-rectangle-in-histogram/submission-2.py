class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0] * n
        right = [n] * n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1

            stack.append(i)

        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]
            else:
                right[i] = n

            stack.append(i)

        maxarea = 0

        for i in range(n):
            width = right[i] - left[i] - 1
            maxarea = max(maxarea, heights[i] * width)
        return maxarea