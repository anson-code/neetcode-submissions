class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = dict()
        for i in nums:
            res[i] = 1 + res.get(i, 0)
        

        freq = [[] for i in range(len(nums)+1)]

        for num, count in res.items():
            freq[count].append(num)

        ans = []

        for i in range(len(freq) - 1, 0 ,-1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans