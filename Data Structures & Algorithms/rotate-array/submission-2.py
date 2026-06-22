class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # j = len(nums) - k
        # for _ in range(k):
        #     nums[i] , nums[j] = nums[j] , nums[i]
        #     i+= 1
        #     j+= 1
        # eg :- [1,2,3,4] k = 2 output :- [3,4,1,2]
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1) #[4,3,2,1]
        reverse(0, k - 1) #[3,4,2,1]
        reverse(k, n - 1) #[3,4,1,2]