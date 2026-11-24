class Solution:
    def trap(self, height: List[int]) -> int:
        maxl , maxr = height[0] , height[-1]

        l , r  = 0 , len(height) - 1 

        water = 0 

        while l < r  :
            if maxl < maxr :
                l +=1 
                maxl = max(height[l] , maxl)
                water += maxl - height[l] 
            
            else:
                r -= 1 
                maxr = max(height[r] , maxr)
                water += maxr - height[r] 
            
        
        return water