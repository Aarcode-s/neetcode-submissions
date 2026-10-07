class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        arr = []
        i, j = 0, 0

        # Merge both sorted arrays
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        # Add remaining elements of nums1
        while i < n1:
            arr.append(nums1[i])
            i += 1

        # Add remaining elements of nums2
        while j < n2:
            arr.append(nums2[j])
            j += 1

        n3 = len(arr)

        # Even number of elements
        if n3 % 2 == 0:
            return (arr[n3 // 2] + arr[n3 // 2 - 1]) / 2

        # Odd number of elements
        else:
            return arr[n3 // 2]