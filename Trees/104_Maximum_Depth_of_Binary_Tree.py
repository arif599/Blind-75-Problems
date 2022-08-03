"""
Problem Statement:
	- given a root, return the maximum depth of the tree
	
Questions:
	1. is the binary tree balanced?
	2. what is the type of the node values?
	3. will the input be a valid binary tree?
	4. can the tree be empty?

Test Cases:
	Input:            3
					/   \
				  9      20	
				         / \
				       15   17
	Ouput: 3
	Explanation: 3 -> 20 -> 17

	Input:            3
	Output: 1
	Explanation: 3 which is the only node

	Input:            
	Output: 0
	Explanation: empty tree

Match:
	- Binary Tree (DFS, BFS)

Plan:
	- DFS
	- get the height of the left subtree and right subtree
	- return the max of the two
	- TC: O(n)
	- SC: O(n)

Optimization:
"""

def DFS(root):
	if root == None:
		return 0
	else:
		return 1 + max(maxDepth(root.left), maxDepth(root.right))

def BFS(root):
	from collection import deque
	queue = deque()
	queue.append(root)
	depth = 0

	while root:
		for i in range(len(queue)):
			currNode = queue.popleft()
			if currNode.left:
				queue.append(currNode.left)
			if currNode.right:
				queue.append(currNode.right)
		depth += 1

	return depth

if __name__ == "__main__":
	pass