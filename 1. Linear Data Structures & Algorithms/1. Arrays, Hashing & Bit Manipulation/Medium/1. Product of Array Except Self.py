class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n^2 traversing, or
        #left to right, then right to left
        '''
        left, right = [1]*len(nums), [1]*len(nums)
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            
        print(left, right)
        ans = []
        
        for i in range(len(nums)):
            ans += [left[i] * right[i]]
            
        return ans'''
        # or
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
            
        print(ans)
            
        pro = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= pro
            pro *= nums[i]
            print(pro)
            
        return ans
