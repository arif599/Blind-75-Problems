"""
Understand:
	Problem Statement:
		- given array of prices, return the maximum profit that can be achieved by buying and selling once

	Questions:
		1. are we guaranteed to make a profit? what if the array is in decresing order?
			- don't buy if profit can't be made
		2. will the array ever be empty?
			- no
		3. will the array contain at least one element?
			- yes
		4. will the array contain all positive numbers?
			- no the prices [0, 10^4]


	Test Cases:
		input: [7,1,5,3,6,4]
		output: 5
		explanation: buy at $1 and sell at $6

		input: [7,6,4,3,1]
		output: 0
		explanation: do not buy and sell

Match:
	- array (sliding window)

Plan:
	- brute force approach
	- have a nested loop that iterates through the array and find two values that give the maximum profit
	- analysis
		- time complexity: O(n^2)
		- space complexity: O(1)

Optimization:
	- sliding window
	- initialize left pointer and global max profit
	- iterate through the array with right pointer and if the current price is greater than price at left pointer then calculate current profit
	- update global max profit if current profit is greater than global max profit
	- update left pointer to point to the right pointer becasue we found a smaller value than the price at left pointer
"""

def maxProfit(prices):
	profit = 0
	left = 0

	for right in range(1, len(prices)):
		if prices[left] < prices[right]:
			currProfit = prices[right] - prices[left]
			profit = max(profit, currProfit)
		else:
			left = right

if __name__ == "__main__":
	pass