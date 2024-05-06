heights = [1,8,6,2,5,4,8,3,7]
output = 49
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxarea = 0
        start = 0
        end = len(height) - 1

        while start < end:
            area = min(height[start], height[end]) * (end - start)
            maxarea = max(maxarea, area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return maxarea

test = Solution()
print(test.maxArea(heights))
