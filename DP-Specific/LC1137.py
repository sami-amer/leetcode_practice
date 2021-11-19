class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        fibs = [0,1,1]
        for i in range(3,n+1):
            fibs.append(fibs[i-1] + fibs[i-2]+fibs[i-3])
        return fibs[-1]





if __name__ == '__main__':
    n = 25 # Output = 1389537
    print(Solution.tribonacci(None,n))