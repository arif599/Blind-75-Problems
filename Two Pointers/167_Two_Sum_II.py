"""
Understand:
	Problem Statement:
		- given an sorted array, find two numbers such that they add up to a specific target
		- return the indices of the two numbers

	Questions:
		1. Will the array ever be empty?
		2. Is the guaranteed to have at least two elements?
		3. What should be returned if the array only has one length?
		4. Is there guaranteed to be a solution?

	Test Cases:
		input: [1,2,3,4,5], target = 7
		output: [2,3]

		input: [1,2,3,4,5], target = 8
		output: [2,4]

Match:
	- sorted array (binary search, two pointers, hash table)

Plan:
	- use a two pointer approach
	- left pointer starts at 0
	- right pointer starts at the end of the array
	- loop to find the target numbers until left pointer is less than right pointer
	- analysis:
		- time complexity: O(n)
		- space complexity: O(1)
		
Optimization:
"""

def twoSum(numbers, target):
	left = 0
	right = len(numbers) - 1

	while left < right:
		curSum = numbers[left] + numbers[right]
		if curSum == target:
			return [left+1, right+1]
		elif curSum < target:
			left += 1
		else:
			right -= 1


if __name__ == "__main__":
	print(twoSum([1,2,3,4,5], 7))