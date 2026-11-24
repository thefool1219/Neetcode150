class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        streak = 0 

        for i in seen:
            if (i-1) not in seen:
                seq = 1 
                while i + seq in seen:
                    seq +=1
                
                streak = max(streak , seq)
        
        return streak