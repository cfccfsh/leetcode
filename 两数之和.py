#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


    def twoSum_2(self, nums, target):
        hash_map = {}
        for item in range(len(nums)):
            if (target - nums[item]) in hash_map:
                return [hash_map[target - nums[item]],item]
            else:
                hash_map[nums[item]] = item


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6

    s = Solution()
    res = s.twoSum_2(nums,target)
    print(res)