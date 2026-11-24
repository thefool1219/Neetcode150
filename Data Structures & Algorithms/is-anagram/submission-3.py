class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        stores , storet = {} , {}

        for i in range(len(s)):
            stores[s[i]] = 1 + stores.get(s[i] , 0 )
            storet[t[i]] = 1 + storet.get(t[i] , 0)
        
        return stores == storet