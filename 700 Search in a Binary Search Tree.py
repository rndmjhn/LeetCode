import json
root1 = [4,2,7,1,3]
val1 = 2

root2 = [4,2,7,1,3]
val2 = 5

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
    


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return root
         

# th = TreeNode.from_list(root1)
# print(th)

test = Solution()
print(test.searchBST(TreeNode.from_list(root1), val1))
print(test.searchBST(TreeNode.from_list(root2), val2))