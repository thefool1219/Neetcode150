class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        ans = []
        for i in nums :
            store[i] += 1 

        for i in range(k):
            ans.append(max(store , key =store.get))
            store.pop(max(store , key= store.get))

        return ans
