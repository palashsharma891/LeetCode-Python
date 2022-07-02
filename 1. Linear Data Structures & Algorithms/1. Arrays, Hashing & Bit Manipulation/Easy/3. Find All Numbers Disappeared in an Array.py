class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            pos = abs(num) - 1
            if nums[pos] > 0:
                nums[pos] *= -1
            
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans += [i+1]
                
        return ans
            
