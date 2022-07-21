"""
Understand:
	Problem Statement:
		- given an height array, find two endpoints that will hold the maximum amount of water
	
	Questions:
		1. is the array guaranteed to have at least two elements?
		2. will there be any negative numbers in the array?
		3. will there be a height of 0 in the array?

	Test Cases:
		input: [1,8,6,2,5,4,8,3,7]
		output: 49

		input: [1,1]
		output: 0	


Match:
	- array (two pointers, sorting)

Plan:
	- brute force approach
	- find all the possible combinations and return the maximum area using a nested for loop
	- analysis:
		- time complexity: O(n^2)
		- space complexity: O(1)

Optimization:
	- using the two pointer approach
	- left pointer starts at 0
	- right pointer starts at the end of the array
	- keep track of maximum area
	- iterate through the array and find the max area
	- analysis:
		- time complexity: O(n)
		- space complexity: O(1)
"""

def containerWithMostWater(height):
	maxArea = 0
	left = 0
	right = len(height) - 1

	while left < right:
		currArea = min(height[left], height[right]) * (right - left)
		maxArea = max(maxArea, currArea)

		if height[left] < height[right]:
			left += 1
		else:
			right -= 1

	return maxArea

if __name__ == "__main__":
	pass