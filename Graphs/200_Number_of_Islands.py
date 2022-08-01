"""

Problem Statement:
	- given a 2D grind find the number of islands
	- island = '1's and water = '0's

Questions:
	1. is the input grid guaranteed to be non-empty?
	2. are we guaranteed to have an island?

Test Cases:
	Input: grid = [
		["1","1","1","1","0"],
		["1","1","0","1","0"],
		["1","1","0","0","0"],
		["0","0","0","0","0"]
	]
	Output: 1

	Input: grid = [
		["1","1","1","0","0"],
		["1","1","0","1","0"],
		["1","1","0","0","0"],
		["0","0","0","0","0"]
	]
	Output: 2

		Input: grid = [
		["1","1","1","0","0"],
		["1","1","0","1","0"],
		["1","1","0","0","0"],
		["0","0","0","1","1"]
		]
	Output: 3

Plan:
	- DFS
	- iterate over the 2D matrix, if we encounter an island and it is not visited then perform DFS
	- increment island counter after finishing DFS
	- TC: O(m*n)
	- SC: O(m*n)

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r, c) not in visited and grid[r][c] == '1':
                   # count += self.dfs(grid, r, c, visited)
                    count += self.bfs(grid, r, c, visited)

        return count
    
    def bfs(self, grid, r, c, visited):
        from collections import deque
        queue = deque()
        queue.append((r, c))

        while queue: 
            curR, curC = queue.popleft() 
            if (curR, curC) not in visited:
                visited.add((curR,curC)) 

                direction = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
                for x, y in direction: 
                    newR = curR + x 
                    newC = curC + y 

                    if (newR >= 0 and newR < len(grid)) and (newC >= 0 and newC < len(grid[newR])):
                        if grid[newR][newC] == "1":
                            queue.append((newR, newC)) 

        return 1

    def dfs(self, grid, r, c, visited):
        if (r, c) in visited:
            return
        else:
            visited.add((r,c))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for x,y in directions:
                newR = r+x
                newC = c+y
                if newR >= 0 and newR < len(grid) and newC >= 0 and newC < len(grid[newR]):
                    if grid[newR][newC] == '1':
                        self.dfs(grid, newR, newC, visited)
            return 1
