class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:
            for i in range(c,target+1):
                if i == c:
                    dp[i].append([c])
                for comb in dp[i-c]:
                    dp[i].append(comb+[c])
        return dp[-1]




if __name__ == "__main__":
    candidates = [2,3,6,7] 
    target = 7