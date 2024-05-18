nums1 = [0,1,0,3,12]   # output [1,3,12,0,0]
nums2 = [0,0,1]   # output [1,0,0]
nums3 = [0,1,0,3,12]   # output [1,3,12,0,0]



class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        popped = 0
        while i < len(nums):
            if nums[i] == 0 and i < len(nums):
                nums.pop(i)
                popped += 1
            else:
                i += 1
        for j in range(popped):
            nums.append(0)
        return nums



test = Solution()
print(test.moveZeroes(nums1))
print(test.moveZeroes(nums2))
print(test.moveZeroes(nums3))
