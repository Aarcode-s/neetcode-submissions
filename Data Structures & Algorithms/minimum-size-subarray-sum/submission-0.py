class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        r = 0
        l =0

        res = float("inf")

        while r < len(nums):
            total += nums[r]
            while total >= target:
                res = min(res , r-l+1)
                total -= nums[l]
                l += 1
            r += 1
        
        return 0 if res == float("inf") else res