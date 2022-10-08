"""
Brute force: 
	- Try all possible combinations of coins and find the min coins
	- Time complexity: O(n^m) where n is the number of coins and m is the amount
	- Space complexity: O(m) where m is the amount

Optimization:
	- DP + memoization
	- Time complexity: O(n*m) where n is the number of coins and m is the amount
	- Space complexity: O(m) where m is the amount
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def countCoins(amount):
            if amount == 0:
                return 1
            if amount in cache:
                return cache[amount]
            
            localCoinMin = float("+inf")
            for coin in coins:
                if amount-coin >= 0:
                    localCoinMin = min(localCoinMin, countCoins(amount-coin)+1)
            
            cache[amount] = localCoinMin
            return cache[amount] 
        
        res = countCoins(amount) - 1
        if res == float("+inf"):
            return -1
        return res