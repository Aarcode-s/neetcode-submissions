class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def rightSmallest(heights: List[int]) -> list[int]:

            stack = []  # (index, value)
            res = [len(heights)] * len(heights)

            for i, h in enumerate(heights):

                while stack and stack[-1][1] > h:
                    ind, val = stack.pop()

                    res[ind] = i

                stack.append((i, h))

            return res

        def leftSmallest(heights: List[int]) -> list[int]:

            stack = []  # (index, value)
            res = [-1] * len(heights)

            for i, h in enumerate(heights):

                while stack and stack[-1][1] >= h:
                    stack.pop()

                if stack:
                    res[i] = stack[-1][0]

                stack.append((i, h))

            return res

        leftIdx = leftSmallest(heights)
        rightIdx = rightSmallest(heights)

        ans = 0

        for i, h in enumerate(heights):

            width = rightIdx[i] - leftIdx[i] - 1

            area = h * width

            ans = max(ans, area)

        return ans