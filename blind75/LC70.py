class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        one_behind = 2
        two_behind = 1
        all_paths = 0

        for i in range(3, n + 1):
            all_paths = one_behind + two_behind
            two_behind = one_behind
            one_behind = all_paths
        return all_paths

if __name__ == '__main__':
    n = 3 #Output = 3
    print(Solution.climbStairs(None, n))