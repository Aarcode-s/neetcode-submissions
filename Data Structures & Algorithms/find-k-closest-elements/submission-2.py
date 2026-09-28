class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l : r + 1]

         # Binary search solution

        # directly jump to mid and calculate

        # left, right = 0, len(arr) - k
        # while left < right:
        #     mid = (left + right) // 2
        #     if x - arr[mid] > arr[mid + k] - x:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return arr[left:left + k]