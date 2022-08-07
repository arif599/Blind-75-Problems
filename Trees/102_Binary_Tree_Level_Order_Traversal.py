# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        from collections import deque
        queue = deque()
        queue.append(root) # 15, 7
        levels = [] # [[3], [9, 20]]
        
        while queue:
            curLevel = [] # 9, 20
            for i in range(len(queue)): # i = 0, 1 -> 1
                curNode = queue.popleft() # 20
                curLevel.append(curNode.val)
                
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right) 
                    
            levels.append(curLevel)
        
        return levels
            
        