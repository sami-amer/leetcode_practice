
def twoSum(nums, target):
        preRes = {}
        for i, num in enumerate(nums):
            preRes[i] = (target - num)
        for j, possible in enumerate(preRes.values()):
            if possible in nums and nums.index(possible) != j:
                return [j, nums.index(possible)]




if __name__ == '__main__':
    print(twoSum([3,2,4],6))