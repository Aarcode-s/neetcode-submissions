class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = []
        
        # for i in range (3):
        #     for _ in nums:
        #         if _ == i:
        #             ans.append(i)
        
        

        for i in nums:
            if i == 0:
                ans.append(i)
        for k in nums:
            if k == 1:
                ans.append(k)

        for z in nums:
            if z == 2:
                ans.append(z)
        nums[:] = ans