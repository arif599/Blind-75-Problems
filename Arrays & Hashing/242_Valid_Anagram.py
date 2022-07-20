"""
Understand:
	Problem Statement:
		- given strings s and t, return true if t is an anagram of s
		- anagrams are words that have the same characters with the same frequency

	Questions:
		1. is an empty string an anagram of another string?
			- string s and t have a minimum length of 1
		2. in order to be an anagram, a part of it is that the length must be the same?
			- if the length is different, they are not anagrams
		3. does the anagram string have to be a valid word?

	Test Cases:
		input: s = "anagram", t = "nagaram"
		output: true

		input: s = "rat", t = "car"
		output: false

		input: s = "aabb", t = "abab"
		output: true

Match:
	- string

Plan:
	- if the length of the strings are different, return false
	- create a character frequency map for s
	- traverse t and decrement the frequency of the character in the map
	- traverse the hashmap and if any of the values are not 0, return false
	- analysis:
		- time complexity: O(s+t)
		- space complexity: O(1) because the hashmap at most can be of size 26 (26 letters in the alphabet)

Optimization:
"""

def isAnagram(s, t):
	sMap = {}
	for char in s:
		if char not in sMap:
			sMap[char] = 1
		else:
			sMap[char] += 1

	for char in t:
		if char not in sMap:
			return False
		else:
			sMap[char] -= 1

	for val in sMap.values():
		if val != 0:
			return False

	return True 

if __name__ == "__main__":
	pass