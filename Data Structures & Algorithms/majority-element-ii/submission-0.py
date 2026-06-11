class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        ans = set()
        for num in nums:
            freq[num] = freq.get(num , 0) +1

            for key, count in freq.items():
                 if count > len(nums)/3:
                    ans.add(key)
        return list(ans)

        


                     
                    
            
            
                