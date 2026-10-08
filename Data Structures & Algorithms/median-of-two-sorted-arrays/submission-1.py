class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # n1 = len(nums1)
        # n2 = len(nums2)

        # # arr = []
        # i, j = 0, 0

        # O(n+m) ---> space complexity
        # O(m+n)

        # Merge both sorted arrays
        # while i < n1 and j < n2:
        #     if nums1[i] < nums2[j]:
        #         arr.append(nums1[i])
        #         i += 1
        #     else:
        #         arr.append(nums2[j])
        #         j += 1

        # # Add remaining elements of nums1
        # while i < n1:
        #     arr.append(nums1[i])
        #     i += 1

        # # Add remaining elements of nums2
        # while j < n2:
        #     arr.append(nums2[j])
        #     j += 1

        # n3 = len(arr)

        # # Even number of elements
        # if n3 % 2 == 0:
        #     return (arr[n3 // 2] + arr[n3 // 2 - 1]) / 2

        # # Odd number of elements
        # else:
        #     return arr[n3 // 2]

        # O(1) ---> space complexity
        # remove the new arr with two variables and a counter variable


        n1 = len(nums1)
        n2 = len(nums2)

        size = n1 + n2

        # Middle indexes
        idx1 = size // 2
        idx2 = size // 2 - 1

        # Store the two middle elements
        element1 = float("-inf")
        element2 = float("-inf")

        i, j = 0, 0
        k = 0

        while i < n1 and j < n2:

            # Pick smaller element
            if nums1[i] < nums2[j]:
                value = nums1[i]
                i += 1
            else:
                value = nums2[j]
                j += 1

            # Check if current index is one of the middle indexes
            if k == idx1:
                element1 = value

            if k == idx2:
                element2 = value

            k += 1

        # Remaining elements from nums1
        while i < n1:

            value = nums1[i]
            i += 1

            if k == idx1:
                element1 = value

            if k == idx2:
                element2 = value

            k += 1

        # Remaining elements from nums2
        while j < n2:

            value = nums2[j]
            j += 1

            if k == idx1:
                element1 = value

            if k == idx2:
                element2 = value

            k += 1

        # Odd length
        if size % 2 == 1:
            return element1

        # Even length
        return (element1 + element2) / 2