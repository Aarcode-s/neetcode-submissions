
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # rows = len(matrix)
        # cols = len(matrix[0])

        # i = 0
        # j = cols - 1

        # while i < rows and j >= 0:

        #     if matrix[i][j] < target:
        #         i += 1

        #     elif matrix[i][j] > target:
        #         j -= 1

        #     else:
        #         return True

        # return False

        rows = len(matrix)
        cols = len(matrix[0])

        start = 0
        end = rows*cols-1

        while start <= end:
            mid = (start+end)//2

            # to change 1-D array index to 2-D array use
            # [mid/cols][mid%cols]

            val = matrix[mid//cols][mid%cols]

            if val > target:
                end = mid-1
            elif val < target:
                start = mid+1
            else:
                return True
        return False

