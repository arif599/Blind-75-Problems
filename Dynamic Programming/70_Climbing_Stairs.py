"""
Problem Statement:
	- find the number of ways to climb n steps

Questions:
	1. is n always positive?

Test Cases:
	Input: n = 2
	Output: 2
	Explanation: There are two ways to climb to the top.
	1. 1 step + 1 step
	2. 2 steps
	Example 2:

	Input: n = 3
	Output: 3
	Explanation: There are three ways to climb to the top.
	1. 1 step + 1 step + 1 step
	2. 1 step + 2 steps
	3. 2 steps + 1 step

Plan:
	- use recursion to find all the number of ways to reach step n
	- at each step, we can either take 1 step or 2 steps
	- if we encounter a step n then return 1
	- TC: O(2^n) because we are making 2 recursive calls at each step
	- SC: O(n) because of the recursive stack

Optimization:
	- we can use memoization to store the number of ways to reach step n
	- TC: O(n) because we only need to calculate the number of ways to reach step n once, eliminating subproblems
	- SC: O(n) because of the recursive stack
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def memoClimbStairs(step):
            if step in cache:
                return cache[step]
            if step == n:
                return 1
            if step > n:
                return 0
            
            cache[step] =  memoClimbStairs(step+1)+memoClimbStairs(step+2)
            
            return cache[step]
        
        return memoClimbStairs(0)