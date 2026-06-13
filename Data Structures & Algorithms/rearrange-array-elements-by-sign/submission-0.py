class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        ans = []

        for x in nums:
            if x >0:
                pos.append(x)
            else:
                neg.append(x)
        
        for i in range (len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        
        return ans