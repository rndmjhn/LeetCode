# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

treenode1 = TreeNode(3,5,1,6,2,9,8,None,None,7,4)
treenode2 = TreeNode(3,5,1,6,7,4,2,None,None,None,None,None,None,9,8)

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root,leaf):
            if not root:
                return 
            if not root.right and not root.left:
                leaf.append(root.val)
            dfs(root.right,leaf)
            dfs(root.left,leaf)
        leaf1,leaf2=[],[]
        dfs(root1,leaf1)
        dfs(root2,leaf2)
        return leaf1==leaf2
    

test = Solution()
print(test.leafSimilar(treenode1, treenode2))
        