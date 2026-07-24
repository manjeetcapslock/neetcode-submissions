class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,num in enumerate(nums):
            comp=target-num
            if comp in dict:
                return [dict[comp],i]
            dict[num]=i 
        