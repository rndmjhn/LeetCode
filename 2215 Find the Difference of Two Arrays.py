nums1 = [1,2,3]
nums2 = [2,4,6]
nums3 = [1,2,3,3]
nums4 = [1,1,2,2]


class Solution:
    def findDifference(self, numsA: list[int], numsB: list[int]) -> list[list[int]]:
        temp1 = []
        temp2 = []
        for i in range(len(numsA)):
            if numsA[i] not in numsB:
                if numsA[i] not in temp1:
                    temp1.append(numsA[i])
        for i in range(len(numsB)):
            if numsB[i] not in numsA:
                if numsB[i] not in temp2:
                    temp2.append(numsB[i])
        
        temp3 = [temp1, temp2]
        return temp3
    
test = Solution()
print(test.findDifference(nums1, nums2))
print(test.findDifference(nums3, nums4))
