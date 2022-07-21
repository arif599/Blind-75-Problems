"""
Understand:
	Problem Statement:
		- given an array representing elevation map
		- width of each bar is 1
		- compute the water that will be trapped between the bars

	Questions:
		1. is the array always guaranteed to trap water? 
		2. will there be any negative numbers in the array?
		3. will there be a height of 0 in the array?

	Test Cases:
		input: [0,1,0,2,1,0,1,3,2,1,2,1]
		output: 6

		height = [4,2,0,3,2,5]
		output: 9

Match:
	- array (two pointers)

Plan:
	- initialize left and right pointers to 0
	- create a waterCount variable to keep track of water trapped
	- iterate until right pointer is at the end of the array
		- increment right pointer by 1
		- if height of right is less than height of left, keep track of the elevation
		- when right pointer is greater than or equal to left pointer, calculate area and subtract the elevation then add to waterCount

Optimization:
"""

def trap(height):
	# incomplete
	waterCount = 0
	elevationCount = 0
	left = 0
	right = 0

	while right < len(height) - 1:
		right += 1
		if height[right] < height[left]:
			elevationCount += height[right]
		else:
			currWaterArea = height[left] * (right - left - 1)
			waterCount += currWaterArea - elevationCount
			left = right
			elevationCount = 0
	
	return waterCount

if __name__ == "__main__":
	print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))