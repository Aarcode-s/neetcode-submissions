class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = []
        
        for i in range (3):
            for _ in nums:
                if _ == i:
                    ans.append(i)
        
        nums[:] = ans