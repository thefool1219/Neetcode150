class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        store = dict()

        for i in s:
            store[i] = store.get(i , 0) + 1 
        
        for i in t :
            store[i] = store.get(i , 0) - 1 
            if store[i] < 0 :
                return False 
        
        return True
