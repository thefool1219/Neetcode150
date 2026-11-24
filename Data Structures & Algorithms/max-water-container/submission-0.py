class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0 
        l , r = 0 , len(heights) -1 

        while l < r :
            distance = (r+1) - (l+1) 

            water = max(min(heights[l] , heights[r]) * distance , water)


            if heights[l] < heights[r]:
                l += 1 
            elif heights[r] < heights[l]:
                r -= 1 
            else:
                l+=1 
                r -= 1

        return water 
