"""
Problem Statement:
	- given a m*n binary matrix 
	- 1 represents land and 0 represents water
	- return the maximum area of island

Questions:
	1. will there ever be a matrix with no land?
	2. can the matrix be empty?

Test Cases:
	Input: grid = [
					[0,0,1,0,0,0,0,1,0,0,0,0,0],
					[0,0,0,0,0,0,0,1,1,1,0,0,0],
					[0,1,1,0,1,0,0,0,0,0,0,0,0],
					[0,1,0,0,1,1,0,0,1,0,1,0,0],
					[0,1,0,0,1,1,0,0,1,1,1,0,0],
					[0,0,0,0,0,0,0,0,0,0,1,0,0],
					[0,0,0,0,0,0,0,1,1,1,0,0,0],
					[0,0,0,0,0,0,0,1,1,0,0,0,0]
				]
	Output: 6
	
Match:
	- Graph (DFS, BFS)

Plan:
	- iterate over the matrix and if the current cell is 1 and not visited, perform BFS
	- BFS and track the area
	- TC: O(mn)
	- SC: O(mn)
"""

def maxAreaOfIsland(grid):
	visited = set()
	maxArea = 0

	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if grid[r][c] == 1 and (r, c) not in visited:
				islandArea = bfs(r, c, grid, visited)
				maxArea = max(islandArea, maxArea)
	return maxArea

def bfs(r, c, grid, visited):
	from collections import deque
	queue = deque()
	queue.append((r,c))
	area = 1

	while queue:
		curR, curC = queue.popleft()

		if (curR, curC) not in visited:
			visited.add((curR, curC))
			area += 1
			direction = [(1,0), (-1,0), (0,1), (0,-1)]
			for dr, dc in direction:
				newR = curR + dr
				newC = curC + dc

				if newR >= 0 and newR < len(grid) and newC >= 0 and newC < len(grid[0]):
					if grid[newR][newC] == 1 and (newR, newC) not in visited:
						queue.append((newR, newC))
	return area - 1

if __name__ == "__main__":
	grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
	print(maxAreaOfIsland(grid))