from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [ 0 for x in range(len(cost) + 1 )] # DP list
        dp[0], dp[1]= 0,0
        for i in range(2, len(cost) + 1):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2]+dp[i-2])
        
        return dp[-1]
            
        
        




if __name__ == '__main__':
    cost = [1,100,1,1,1,100,1,1,100,1]
    # Output = 6
    # cost = [10,15,20]
    print(Solution.minCostClimbingStairs(None, cost))