class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        # Two pointers: start from both ends
        l, r = 0, len(height) - 1

        # Maximum height seen from the left and right
        leftMax = height[l]
        rightMax = height[r]

        # Total trapped water
        res = 0

        while l < r:

            # Left side is the limiting boundary
            if leftMax < rightMax:
                l += 1

                # Update the maximum height from the left
                leftMax = max(leftMax, height[l])

                # Water = left boundary - current height
                res += leftMax - height[l]

            # Right side is the limiting boundary
            else:
                r -= 1

                # Update the maximum height from the right
                rightMax = max(rightMax, height[r])

                # Water = right boundary - current height
                res += rightMax - height[r]

        return res