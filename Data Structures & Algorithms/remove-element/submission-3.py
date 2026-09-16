class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if val not in nums:
            return len(nums)
        
        first, second = 0, 1
    

        while first < len(nums) and second < len(nums):

            if nums[first] == val:
                if nums[second] != val:
                    nums[first], nums[second] = nums[second], nums[first]
                    
                else:
                    second += 1
            else:
                first += 1
                second += 1
        return first

