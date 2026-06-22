class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first using division operation
        # output =[]
        # product = 1
        # for num in nums:
        #     product *= num
        # print ( product)
        # for i in range(len(nums)):
        #     if nums [i] != 0:
        #         output.append(product//nums[i])
        #     else:
        #          output.append(product)
        # return output
        zeroCount = 0
        total = 1
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                total *= num

        for i in range(len(nums)):

            if zeroCount > 1:
                nums[i] = 0

            elif zeroCount == 1:
                nums[i] = total if nums[i] == 0 else 0

            else:
                nums[i] = total // nums[i]

        return nums

            
