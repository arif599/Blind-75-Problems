"""
Understand:
	Problem Statement:
		- given an array of strings, group anagrams together
		- anagrams are words that have the same characters with the same frequency

	Questions:
		1. is an empty string an anagram of another string?
			- no, empty strings are grouped together
		2. will the input array ever be empty?
			- no, the input array will have a minimum length of 1
		3. will the input array ever have a single element?
			- yes

	Test Cases:
		input: ["eat", "tea", "tan", "ate", "nat", "bat"]
		output: [["ate", "eat","tea"], ["nat","tan"], ["bat"]]

		input: [""]
		output: [[""]]

		input: ["a"]
		output: [["a"]]

		input: ["a", "b"]
		output: [["a"], ["b"]]

Match:
	- array (sliding window, two pointers, sorting, traversing, hashmap)

Plan:
	- iterate thorugh the array and sort each string
	- iterate through the sorted array and create a hashmap where key = sorted string, value = index of the string in the array
	- iterate through the hashmap and generate the results array
	- analysis:
		- n = len(nums)
		- s = len(largest string in nums)
		- time complexity: O(n*slogs)
		- space complexity: O(n)

Optimization:
"""

def groupAnagrams(strs):
	groupMap = {}

	for i in range(len(strs)):
		sortedStr = "".join(sorted(strs[i])) # sort each string and getting the key

		# check if key in hashmap and store the word
		if sortedStr not in groupMap:
			groupMap[sortedStr] = [strs[i]]
		else:
			groupMap[sortedStr].append(strs[i])
	
	return groupMap.values() # return a list of values of the hashmap

if __name__ == "__main__":
	groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])