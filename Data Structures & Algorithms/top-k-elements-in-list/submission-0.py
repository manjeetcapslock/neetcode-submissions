class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums:
            dict[i]=dict.get(i,0)+1
        arr = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        ans = []

        for i in range(k):
            ans.append(arr[i][0])

        return ans

        