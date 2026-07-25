class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l1=[1]*len(nums)
        psum=1
        for i in range(len(nums)):
            l1[i]=psum
            psum=psum*nums[i]
        ssum=1
        for i in range(len(nums)-1,-1,-1):
            l1[i]=l1[i]*ssum
            ssum=ssum*nums[i]
        return l1
        