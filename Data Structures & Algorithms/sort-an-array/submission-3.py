class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid_index=len(nums)//2
        left=self.sortArray(nums[:mid_index])
        right=self.sortArray(nums[mid_index:])
        return self.merge(left,right)      

    def merge(self,list1,list2):
        result=[]
        i,j=0,0
        while i<len(list1) and j < len(list2):
            if list1[i]<=list2[j]:
                result.append(list1[i])
                i=i+1
            else:
                result.append(list2[j])
                j=j+1
        while i< len(list1):
            result.append(list1[i])
            i=i+1
        
        while j < len(list2):
            result.append(list2[j])
            j=j+1
        
        return result
