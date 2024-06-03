


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


root1 = [3,9,20,None,None,15,7]
root2 = [1,None,2]

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
           return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth,right_depth) + 1
                       
    

test = Solution()
print(test.maxDepth(root1))
print(test.maxDepth(root2))