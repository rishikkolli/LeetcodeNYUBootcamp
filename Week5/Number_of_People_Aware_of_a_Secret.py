class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[1] = 1  
        
        for day in range(1, n + 1):
            for start_day in range(day - forget + 1, day - delay + 1):
                if start_day > 0:
                    dp[day] = (dp[day] + dp[start_day]) % MOD
        
        total = 0
        for day in range(n - forget + 1, n + 1):
            if day > 0:
                total = (total + dp[day]) % MOD
        
        return total
