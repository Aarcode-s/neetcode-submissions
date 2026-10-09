
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            # Found
            if nums[mid] == target:
                return True

            # Handle duplicates
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # Left side is sorted
            if nums[low] <= nums[mid]:

                # Target is in left side
                if nums[low] <= target < nums[mid]:
                    high = mid - 1

                # Otherwise go right
                else:
                    low = mid + 1

            # Right side is sorted
            else:

                # Target is in right side
                if nums[mid] < target <= nums[high]:
                    low = mid + 1

                # Otherwise go left
                else:
                    high = mid - 1

        return False
