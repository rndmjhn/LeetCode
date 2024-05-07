heights = [0,1,0,2,1,0,1,3,2,1,2,1]
# output = 6

# we'll end up using some part of #11 container with most water to find areas that can hold water but will
# need to modify it to acount for all inner blocks 
class Solution:
    def trap(self, height: list[int]) -> int:
        