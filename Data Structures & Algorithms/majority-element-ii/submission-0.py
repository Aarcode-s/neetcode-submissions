class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        output = []

        for key in hashmap:
            if hashmap[key] > n / 3:
                output.append(key)

        return output