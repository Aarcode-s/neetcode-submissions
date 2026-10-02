class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        stack = []  # (index, temperature)

        for i, r in enumerate(temperatures):

            while stack and r > stack[-1][1]:
                stackInd, stackval = stack.pop()
                res[stackInd] = i - stackInd

            stack.append((i, r))

        return res