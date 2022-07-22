"""
Understand:
	Problem Statement:
		- Given a string s, find the length of the longest substring without repeating characters

	Questions:
		1. will the string ever be empty?
			- yes
		2. what is the input string contained all the same characters? ex: "aaaaa"?
			- return 1
		3. will the string contain digits, symbols, and spaces?
			- yes

	Test Cases:
		input: "abcabcbb"
		output: 3
		explanation: the answer is "abc", with the length of 3

		input: "bbbbb"
		output: 1
		explanation: the answer is "b", with the length of 1

Match:
	- string (sliding window, hashmap/set)

Plan:
	- sliding window
	- initiate left pointer and loop with right pointer to traverse the array
	- keep a set to track visited characters for the current window
	- keep track of the length of the substring
	- update max length
	- analysis:
		- time complexity: O(n)
		- space complexity: O(n)

Optimization:
"""

def lengthOfLongestSubstring(s):
	maxLength = 0
	currLength = 0
	left = 0
	visited = set()

	for right in range(len(s)):
		if s[right] in visited:
			while s[right] in visited:
				visited.remove(s[left])
				left += 1
				currLength -= 1

		visited.add(s[right])
		currLength += 1
		maxLength = max(maxLength, currLength)

	return maxLength

if __name__ == "__main__":
	print(lengthOfLongestSubstring("abcabcbb"))