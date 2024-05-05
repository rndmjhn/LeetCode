heights = [1,8,6,2,5,4,8,3,7]
output = 49



class Solution:
    def maxArea(self, height: list[int]) -> int:
        currentmax = [0, 0, 0]
        start = 0
        end = len(height) -1
        flipper = False
        while start < end:
            print(currentmax)
            if (((end + 1) - (start + 1)) * min(height[start], height[end])) > currentmax[2]:
                currentmax[0], currentmax[1], currentmax[2] = start, end, ((end + 1) - (start + 1)) * min(height[start], height[end])
                if flipper:
                    start += 1
                    flipper = False
                else:
                    end -= 1
                    flipper = True
                continue
            else:
                if flipper:
                    start += 1
                    flipper = False
                else:
                    end -= 1
                    flipper = True
                continue
            print(currentmax)


test = Solution()
print(test.maxArea(heights))
