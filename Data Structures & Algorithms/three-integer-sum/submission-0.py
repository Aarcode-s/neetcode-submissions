class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first sort the array then no need to use sort for triplet as everything will be in sorted order 
        # then we will iterate using two pointer approach since we have to find triplet we will use three variable i , j , k  
        # we will first fix i and fid the other thgen increase i and do till all are found

        ans = []
        n = len(nums)

        nums.sort()  # actually call sort()

        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1  # right pointer start at the end

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum < 0:
                    j += 1

                elif total_sum > 0:
                    k -= 1

                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)

                    j += 1
                    k -= 1

                    # Skip duplicates
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans
