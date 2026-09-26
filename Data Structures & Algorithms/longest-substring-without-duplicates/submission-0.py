class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     
        max_heap = {}

        maxi = 0
        count = 0

        i, j = 0, 0

        while j < len(s):
            if s[j] not in max_heap:
                max_heap[s[j]] = j
                count += 1
                j += 1
            else:
                i = max(i ,max_heap[s[j]] + 1)
                max_heap[s[j]] = j
                count = j - i + 1
                j += 1

            maxi = max(count, maxi)

        return maxi