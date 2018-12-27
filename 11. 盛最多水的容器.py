class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_a = 0
        while left < right:
            if height[left] <= height[right]:
                tmp = (right - left) * height[left]
                left += 1
            else:
                tmp = (right - left) * height[right]
                right -= 1
            max_a = max(max_a, tmp)
        return max_a


h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
s = Solution()
r = s.maxArea(h)
print(r)
