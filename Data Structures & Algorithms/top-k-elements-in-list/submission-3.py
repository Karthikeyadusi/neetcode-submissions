class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        values = []
        sort = []
        ans = []
        for num in nums:
            h[num] = h.get(num, 0) + 1
        for key in h:
            values.append(h[key])
        sort = sorted(values)[::-1]
        for key in h:
            for i in range(0,k):
                if h[key] == sort[i]:
                    ans.append(key)
                    break
        return ans
    
            
          
