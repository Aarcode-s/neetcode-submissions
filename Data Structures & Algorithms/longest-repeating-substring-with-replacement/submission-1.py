class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi = 0
        count = {}
        left = 0
        answer = 0

        for j in range(len(s)):
            count[s[j]] = count.get(s[j] , 0)+1

            maxi = max(maxi , count[s[j]])

            if j-left+1 - maxi > k:
                count[s[left]] -= 1
                left += 1
            
            answer = max(answer , j-left+1)

        return answer
