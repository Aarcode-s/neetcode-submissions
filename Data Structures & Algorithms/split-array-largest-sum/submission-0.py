class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        # Minimum possible answer: largest element
        l = max(nums)

        # Maximum possible answer: sum of all elements
        r = sum(nums)

        res = r

        def split(max_sum):
            # Start with one subarray
            pieces = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > max_sum:
                    # Start a new subarray
                    pieces += 1
                    current_sum = num
                else:
                    current_sum += num

            # Can we split into at most k subarrays?
            return pieces <= k

        while l <= r:
            mid = l + (r - l) // 2

            if split(mid):
                # This maximum sum is possible.
                res = mid

                # Try to find a smaller maximum sum.
                r = mid - 1
            else:
                # Maximum sum is too small.
                # We need a larger limit.
                l = mid + 1

        return res