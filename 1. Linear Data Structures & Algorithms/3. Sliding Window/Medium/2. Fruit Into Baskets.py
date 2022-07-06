class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        # 0 1 2 3 4 5 6
        #[0,0,1,1,0,2,3]
        
        l, r = 0, 0
        max_len = 0
        d = {}
        
        for r in range(len(fruits)):
            #storing the last index fruits[r] was seen at
            d[fruits[r]] = r
            
            if len(d) >= 3:
                
                # find the farthest last seen fruit to left, 1 in our case
                min_val = min(d.values())
                
                # delete the farthest fruit, 1 in our case
                del d[fruits[min_val]]
                
                # move left pointer to the index after deleted fruit, index 4 in our case
                l = min_val + 1
                
            max_len = max(max_len, r - l + 1)
            
        return max_len
