class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            if n not in res:
                res[n] = 0
            res[n] += 1
        return sorted(res, key=res.get, reverse = True)[:k]
