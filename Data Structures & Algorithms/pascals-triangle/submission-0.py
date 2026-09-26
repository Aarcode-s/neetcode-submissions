class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows

        result = [[1]]

        for i in range(1, n):
            ele = [1]

            j = 1

            while j < i:
                toAdd = result[i - 1][j - 1] + result[i - 1][j]
                ele.append(toAdd)
                j += 1

            ele.append(1)
            result.append(ele)
        return result