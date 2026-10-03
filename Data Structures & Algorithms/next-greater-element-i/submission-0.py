class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        next_greater = {}

        for num in nums2:

            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num

            stack.append(num)

        # Elements remaining in stack have no greater element
        while stack:
            num = stack.pop()
            next_greater[num] = -1

        return [next_greater[num] for num in nums1]