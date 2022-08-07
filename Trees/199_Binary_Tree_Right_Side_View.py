# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        from collections import deque
        queue = deque()
        queue.append(root) # queue = []
        output = [] # output = [1, 3, 4]
        
        while queue:
            length = len(queue)
            for i in range(length): # i = 1 < 2
                curNode = queue.popleft() # curNode = 4
                
                if i == length - 1:
                    output.append(curNode.val) 
                    
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                    
        return output