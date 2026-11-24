class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums :
            return False 
        
        seen = set(nums)

        return (len(nums)) > (len(seen))