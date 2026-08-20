class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        left = 0
        best = 0
        maximum = 0
        for right in range(0,len(s)):
            adding = s[right]
            h[adding] = h.get(adding, 0) + 1
            maximum = max(maximum, h[adding])
            valid = (right-left+1) - maximum
            while valid>k:
                h[s[left]]-=1
                if h[s[left]] == 0:
                    del h[s[left]]
                left+=1
                valid = (right-left+1) - maximum
            best = max(best, right-left+1)
        return best