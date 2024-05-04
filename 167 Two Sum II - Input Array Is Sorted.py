numbers1 = [2,7,11,15]
target1 = 9
numbers2 = [2,3,4]
target2 = 6
numbers3 = [-1,0]
target3 = -1

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start = 0
        end = len(numbers) - 1
        while numbers[start] < numbers[end]:
            if numbers[start] + numbers[end] == target:
                ans = [start + 1, end + 1]
                return  ans
            elif numbers[start] + numbers[end] <= target:
                start += 1
                continue
            elif numbers[start] + numbers[end] >= target:
                end -= 1
                continue

test = Solution()
print(test.twoSum(numbers1, target1))