class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
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
        """
        
        # time complexity = O(n X m) n = size of array s2 and m is dictionary size
        # space complexity = O(n)

        # OPTIMISED
        if len(s1)>len(s2):
            return False
            
        s1_count = [0]*26
        window_count = [0]*26

        # character mapping for s1

        for char in s1:
            index = ord(char) - ord("a")
            s1_count[index] += 1
        
        # checking first window

        for char in s2[:len(s1)]:
            index = ord(char) - ord("a")
            window_count[index] += 1

        if s1_count == window_count:
            return True
        
        # checking while sliding window

        for j in range(len(s1) , len(s2)):

            index = ord(s2[j]) - ord("a")
            window_count[index] += 1

            # remove mapping of previous start so it moves
            index = ord(s2[j-len(s1)]) - ord("a")
            window_count[index] -= 1

            

            if window_count == s1_count:
                return True
        return False

    
    
    

        

























