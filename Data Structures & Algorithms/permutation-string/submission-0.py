class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}

        for i in s1:
            s1_map[i] = s1_map.get(i , 0)+1
        
        s2_map = {}

        i = 0
        j = len(s1)

        while j <= len(s2):
            for k in s2[i:j]:
                s2_map[k] = s2_map.get(k , 0)+1
            
            if s2_map == s1_map:return True
            else:
                i+=1
                j += 1 
                s2_map.clear()
        return False