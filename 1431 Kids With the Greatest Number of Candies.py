candies1 = [2,3,5,1,3]
extraCandies1 = 3
candies2 = [4,2,1,1,2]
extraCandies2 = 1
candies3 = [12,1,12]
extraCandies3 = 10

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        i = 0
        while i < len(candies):
            if (candies[i] + extraCandies) >= max(candies):
                result.append(True)
            else:
                result.append(False)
            i += 1

        return result
    

test = Solution()
print(test.kidsWithCandies(candies1, extraCandies1))
print(test.kidsWithCandies(candies2, extraCandies2))
print(test.kidsWithCandies(candies3, extraCandies3))