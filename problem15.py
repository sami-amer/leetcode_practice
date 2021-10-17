from typing import DefaultDict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # hash 2 sum in O(n^2) and then iterate in O(n) for O(n^2)?
        answer = []
        twoSum = DefaultDict()
        for i in range(len(nums)):
            for j in range(len(nums)):
                twoSum[nums[i] + nums[j]] = str(nums[i]) + ',' +str(nums[j])
        for num in nums:
            if -num in twoSum:
                unpacked = [*twoSum[-num].split(",")]
                answer.append([num, int(unpacked[0]), int(unpacked[1])])
        return answer





if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(Solution.threeSum(None,nums))