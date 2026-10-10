
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def notCaught(piles: List[int], h: int, bph: int) -> bool:
            hours = 0

            for pile in piles:
                hours += pile // bph

                if pile % bph != 0:
                    hours += 1

            return hours <= h

        low = 1
        high = max(piles)

        while low < high:
            bph = (low + high) // 2

            if notCaught(piles, h, bph):
                high = bph
            else:
                low = bph + 1

        return low
