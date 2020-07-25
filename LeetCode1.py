class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            if target - nums[i] in nums and i != nums.index(target - nums[i]):
                return i,nums.index(target - nums[i])

    def twoSum_2(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            elif target - nums[i] in dict and dict[target - nums[i]] != i:
                return dict[target - nums[i]],i

def main():
    nums = [2,7,11,15]
    target = 9
    a = Solution()
    print(a.twoSum_2(nums,target))

if __name__ == "__main__":
    main()

