import json


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Shrink the long json string by removing unnecessary lines
        t = '\n'.join([l for l in self.json_repr.split('\n')
            if '[' not in l and ']' not in l])
        return t.replace(',','')

    @property
    def json_repr(self):
        if self.val is None:
            return 'None'
        # Recursively construct a json-compliant representation
        if self.left is None:
            text = f"[{self.val}]"
        else:
            text = f"[{self.val}, [{self.left.json_repr}, {self.right.json_repr}]]"
        return json.dumps(json.loads(text), indent=1)

    def from_list(l):
            nodes = [TreeNode(v) for v in l]
            kids = nodes[::-1]
            root = kids.pop()
            for node in nodes:
                if node:
                    if kids:
                        node.left = kids.pop()
                    if kids:
                        node.right = kids.pop()
            return root


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
print(test.maxDepth(TreeNode.from_list(root1)))
print(test.maxDepth(TreeNode.from_list(root2)))