# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        maxPath = [] # [3, 4, 5]
        count = 0 # 4
        
        def dfs(root): # root = 3, 4, 5
            if root == None:
                return
        
            if len(maxPath) == 0:
                maxPath.append(root.val)
            else:
                maxPath.append(max(maxPath[-1], root.val))
                
            if root.val == maxPath[-1]:
                nonlocal count
                count += 1
                
            dfs(root.left)
            dfs(root.right)
            
            maxPath.pop()
        
        dfs(root)
        return count