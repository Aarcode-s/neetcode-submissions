class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for _ in range(k):
            if not count:
                break

            key = max(count, key=count.get)
            ans.append(key)
            count.pop(key)

        return ans