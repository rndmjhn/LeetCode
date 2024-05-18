gain1 = [-5,1,5,0,-7]
output1 = 1
gain2 = [-4,-3,-2,-1,4,3,2]
output2 = 0

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        start = 0
        max = 0
        for i in range(len(gain)):
            start = start + gain[i]
            if start > max:
                max = start
        return max


test = Solution()
print(test.largestAltitude(gain1))
print(test.largestAltitude(gain2))