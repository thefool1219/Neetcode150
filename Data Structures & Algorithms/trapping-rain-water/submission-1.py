class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n == 0 :
            return 0 

        l , r = 0 , n-1 
        highl , highr = height[l] , height[r]
        
        water = 0 

        while l < r :
            if highl < highr:
                l += 1 
                highl = max(height[l] , highl)
                water += highl - height[l]
            
            else:
                r -= 1 
                highr = max(height[r] , highr)
                water += highr - height[r]
            
        
        return water


            