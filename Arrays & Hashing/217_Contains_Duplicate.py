"""
Understand:
	Problem Statement:
		- Given an array of integers, find if the array contains any duplicates

	Questions:
		1. What if the array is empty?  
			- Based on the constraints, the array will have a minimum length of 1

	Test Cases:
		input: [1,2,3,4,5]
		output: False

		input: [1,1,2,3,4,5]
		output: True

		input: [1]
		output: True

Match:
	- array (sliding window, two pointers, sorting, traversing, hashmap)

Plan:
	- create a set to store the values
	- traverse the list and check if the element is in the set 
	- analysis:
		- time complexity: O(n)
		- space complexity: O(n)

Optimization:
"""

def containsDuplicates(nums):
	visited = set()

	for num in nums:
		if num not in visited:
			visited.add(num)
		else:
			return True

	return False

if __name__ == "__main__":
	print(containsDuplicates([1,2,3,4,5]))
	print(containsDuplicates([1,1,2,3,4,5]))