# Given an integer array nums, return true if any 
# value appears at least twice in the array, 
# and return false if every element is distinct.

nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

if len(nums1) != len(set(nums1)):
    print("found Duplicates! in nums1") 
    
if len(nums2) != len(set(nums2)):
    print("found Duplicates! in nums2")

if len(nums3) != len(set(nums3)):
    print("found Duplicates! in nums3")