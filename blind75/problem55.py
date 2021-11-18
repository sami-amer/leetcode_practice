from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0

        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, n + i)
        return True




if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print(Solution.canJump(None,nums))
        