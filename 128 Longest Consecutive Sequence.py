

nums1 = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
nums3 = [1,2,0,1]




class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        table = {}
        maxval = 0
        for num in nums:
            x = table.get(num - 1, 0)
            y = table.get(num + 1, 0)
            val = x + y + 1
            table[num - x] = val
            table[num + y] = val
            maxval = max(maxval, val)
        return maxval
    
test = Solution()
print(test.longestConsecutive(nums1))
print(test.longestConsecutive(nums2))
print(test.longestConsecutive(nums3))