"""
Understand:
	Problem Statement:
		- given an unsorted array return the length of the longest consecutive element sequence

	Questions:
		1. Will the array ever be empty?
			- yes
		2. what should be returned if the array is empty?
			- 0

	Test Cases:
		input: [100, 4, 200, 1, 3, 2]
		output: 4

		input: [1, 2, 3, 4]
		output: 4

		input: [5, 4, 3, 2, 1, 100, 101, 102]
		output: 5

Match:
	- array

Plan:
	- sort array
	- traverse the array looking for consecutive elements
	- consective elements are greater then 1 compared to the previous element
	- keep track of max count
	- analysis:
		- time complexity: O(nlog(n))
		- space complexity: O(1)

Optimization:
	- convert list to set
	- try to find the start of a sequence if  num - 1 is not in set
	- loop till num+i is not in set and increment count
	- analysis:
		- time complexity: O(n)
		- space complexity: O(n)
"""

def longestConsecutive(nums):
	if len(nums) == 0:
		return 0
	
	numSet = set(nums)
	maxCount = 0

	# check if the element is the start of a sequence
	for num in nums:
		if num-1 not in numSet:
			curCount = 1
			while num+curCount in numSet:
				curCount += 1
			maxCount = max(maxCount, curCount)

	return maxCount

	
if __name__ == "__main__":
	pass