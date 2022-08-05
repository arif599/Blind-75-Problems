"""
Understand:
	Problem Statement:
		- given a string s and an integer k
		- find the longest substring containing the same letters given you can change any character by at most k times
	
	Questions:
		1. will the string be empty?
		2. do we have to perform the operation k times or at most k times?
		3. will k be greater than the length of the string?
		4. will the string contain digits, symbols, and spaces?

	Test Cases:
		input: "aab", 1
		output: 3
		explanation: the longest substring is "aaa", with the length of 3

		input: "aba", 2
		output: 3
		explanation: the longest substring is "bbb", with the length of 3

Match:
	- sliding window (character frequency hashmap)

Plan:
	- sliding window approach
	- use a hashmap to track the frequency of each character in the window
	- replace a character with k 
Optimization:
"""

def characterReplacement(s, k):
	currLength = 0
	maxLength = 0
	left = 0
	freqCharMap = {}

	for right in range(len(s)):
		if s[right] not in freqCharMap:
			if len(freqCharMap) == 2:
				count = min(freqCharMap.values())
				if count <= k:
					currLength += count
				else:
					currLength += k

			freqCharMap[s[right]] = 1
			while len(freqCharMap) > 2:
				if freqCharMap[s[left]] == 0:
					del freqCharMap[s[left]]
				else:
					currLength -= 1
					freqCharMap[s[left]] -= 1
		else:
			freqCharMap[s[right]] += 1
			currLength += 1

		maxLength = max(maxLength, currLength)

	return maxLength
			
if __name__ == "__main__":
	print(characterReplacement("ABAB", 2))