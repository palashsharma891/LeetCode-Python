class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i, j = 0, len(nums)-1
        while True:
            print(i, j)
            s = nums[i] + nums[j]
            if s == target:
                return True # if index not asked, you can use two pointers
            if s < target:
                i += 1
            else:
                j -= 1
