class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

nums = [3,3]
target = 6
np = Solution()
output2 = np.twoSum(nums,target)
print(output2)