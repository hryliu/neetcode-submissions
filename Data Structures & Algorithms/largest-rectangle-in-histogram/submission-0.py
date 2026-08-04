class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # push elements onto stack (height, index)
        # while curr element is smaller than element on top of stack, pop and compute area
        # track max area

        stack = deque() # height, index
        max_area = 0
        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][0]:
                prev_height, prev_index = stack.pop()
                max_area = max(max_area, prev_height * (i - prev_index))
                start = prev_index

            stack.append((heights[i], start))

        while stack:
            height, index = stack.pop()
            max_area = max(max_area, height * (len(heights) - index))

        return max_area




        