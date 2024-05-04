# Given an integer array nums, return an array answer 
# such that answer[i] is equal to the product of all the 
# elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed 
# to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and
# without using the division operation.

nums = [1,2,3,4]
# Output: [24,12,8,6]
# nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        a=[1]*n
        for i in range(n-2, -1, -1):
            a[i]=nums[i+1]*a[i+1]
        b=1
        for j in range(1,n):
            b*=nums[j-1]
            a[j]*=b
        return a

test = Solution()
print(test.productExceptSelf(nums))