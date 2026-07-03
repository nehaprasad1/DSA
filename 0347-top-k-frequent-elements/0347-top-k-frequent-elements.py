class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cat =  Counter(nums)
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])
        for num , fq in cat.items():
            buckets[fq].append(num)
        ans = []
        for f in range(len(buckets)-1,0,-1):
            for n in buckets[f]:
                ans.append(n)
                if len(ans)==k:
                    return ans




