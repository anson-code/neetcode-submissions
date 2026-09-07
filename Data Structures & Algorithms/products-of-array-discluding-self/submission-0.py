class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        sub = 1

        for i in range(0,len(nums)-1):
            res.append(res[-1]*nums[i])

        for i in range(len(nums)-1,-1,-1):
            res[i] *= sub
            sub *= nums[i]

        return res