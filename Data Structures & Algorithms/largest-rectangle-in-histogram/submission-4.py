class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        stack = []

        for i in range(len(heights)):
            start = i

            while stack and heights[i] < stack[-1][1]:
                index, height_bound = stack.pop()
                start = index
                width = i - start
                height = height_bound
                max_area = max(max_area, width * height)

            stack.append((start, heights[i]))

        while stack:
            index, height = stack.pop()
            width = len(heights) - index
            max_area = max(max_area, width * height)

        return max_area