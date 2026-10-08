class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        def binary (nums:list[int] , target:int ,leftside:bool):
            left , right = 0 , len(nums)-1
            idx = -1

            while (left<=right) :
                mid = (left + right) //2

                if nums[mid] == target:
                    idx = mid 
                    if leftside:
                        right = mid -1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return idx
        
        left = binary(nums , target , True)
        right = binary(nums , target , False)
        return [left, right]
