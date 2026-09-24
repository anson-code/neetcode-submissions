class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l, r = 0, len(heights) - 1

        while r > l:
            ans = max((r - l) * min(heights[l],heights[r]), ans)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return ans