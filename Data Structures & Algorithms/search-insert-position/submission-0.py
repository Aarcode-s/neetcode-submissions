class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:

                if mid == high:
                    return mid + 1

                if nums[mid + 1] > target:
                    return mid + 1
                else:
                    low = mid + 1

            else:

                if mid == low:
                    return mid

                if nums[mid - 1] < target:
                    return mid
                else:
                    high = mid - 1


