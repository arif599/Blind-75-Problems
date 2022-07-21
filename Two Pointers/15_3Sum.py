"""
Understand:
	Problem Statement:
		- given an array return all triplets that add up to 0
		- return all possible triplets

	Questions:
		1. Is the array guaranteed to have at least three elements?
		2. what to return if there are no triplets that add up to 0?

	Test Cases:
		input: [-1, 0, 1, 2, -1, -4]
		output: [[-1, 0, 1], [-1, -1, 2]]

		input: [0,1,1]
		output: []

Match:
	- array (two pointers, sorting)
	- 2 sum

Plan:
	- sort the array
	- for every element, find 2 numbers that add up to 0 (perform two pointers)
	- analysis:
		- time complexity: O(n^2) + O(nlogn)
		- space complexity: O(1)

Optimization:
"""

def threeSum(nums):
	result = []
	nums.sort()

	for i, num in enumerate(nums):
		if i > 0 and num == nums[i - 1]:
			continue

		# two sum
		left = i + 1
		right = len(nums) - 1
		while left < right:
			curSum = num + nums[left] + nums[right]
			if curSum == 0:
				result.append([num, nums[left], nums[right]])
			elif curSum > 0:
				right -= 1
			else:
				left += 1

	return result

if __name__ == "__main__":
	print(threeSum([-1, 0, 1, 2, -1, -4]))