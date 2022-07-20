"""
Understand:
	Problem Statement:
		- given an integer array return the top k most frequent elements
		- order doesn't matter when returning the top k elements

	Questions:
		1. Will the array ever be empty?
			- no, it will always have at least one element
		2. will k ever be greater than the length of the array?
			- no, it will always be less than or equal to the length of the array
		3. will the elements in the array be sorted?

	Test Cases:
		input: [1, 1, 1, 2, 2, 3], k = 2
		output: [1, 2]

Match:
	- array
	- hash table

Plan:
	- create a frequency hash map from the array
	- sort the hashmap by value and return the top k elements
	- analysis:
		- time complexity: O(nlogn)
		- space complexity: O(n)

Optimization:
	- heaps? O(klogn)
	- modified bucket sort? O(n)
		- create a frequency hash map from the array
		- create an array of size n where the indeces represent the frequency of the element
		- iterate through the frequency array backwards and get k elements
"""

def topKFrequent(nums, k):
	frequency_map = {}
	frequency_list = [[] for i in range(len(nums)+1)]

	for num in nums:
		if num in frequency_map:
			frequency_map[num] += 1
		else:
			frequency_map[num] = 1

	for char, count in frequency_map.items():
		frequency_list[count].append(char)

	result = []
	for i in range(len(frequency_list)-1, -1, -1):
		for char in frequency_list[i]:
			result.append(char)
			if len(result) == k:
				return result


if __name__ == "__main__":
	pass