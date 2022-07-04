class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        pro = 1
        l, ans = 0, 0
        
        for r in range(len(nums)):
            pro *= nums[r]
            while pro >= k and l <= r:
                pro /= nums[l]
                l += 1
            ans += r - l + 1
            
        return ans
