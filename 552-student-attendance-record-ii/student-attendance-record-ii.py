class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # dp[absence_count][consecutive_lates]
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1  # Base case: 1 way to have an empty record
        
        for _ in range(n):
            new_dp = [[0] * 3 for _ in range(2)]
            
            # Transition for 'P' (Present): resets consecutive lates
            for a in range(2):
                for l in range(3):
                    new_dp[a][0] = (new_dp[a][0] + dp[a][l]) % MOD
            
            # Transition for 'L' (Late): increments consecutive lates by 1
            for a in range(2):
                for l in range(2):
                    new_dp[a][l + 1] = (new_dp[a][l + 1] + dp[a][l]) % MOD
            
            # Transition for 'A' (Absent): resets consecutive lates, absence goes from 0 to 1
            for l in range(3):
                new_dp[1][0] = (new_dp[1][0] + dp[0][l]) % MOD
                
            dp = new_dp
            
        # Sum up all valid states after n days
        total_ways = 0
        for a in range(2):
            for l in range(3):
                total_ways = (total_ways + dp[a][l]) % MOD
                
        return total_ways