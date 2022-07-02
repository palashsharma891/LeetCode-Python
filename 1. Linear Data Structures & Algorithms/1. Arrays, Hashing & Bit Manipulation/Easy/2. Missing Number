class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1. hash map O(n) O(n)
        # 2. sort and search O(nlogn) O(1)
        # or sum of array
        l = len(nums)
        s = (l * (l + 1)) // 2
        return s - sum(nums)
    
    # O(n) O(1)
