class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)

        # count frequency of each num
        frequency = {}
        for n in nums:
            if n not in frequency:
                frequency[n] = 1
            else:
                frequency[n] += 1

        # place numbers in buckets
        buckets = [[] for n in range(len(nums) + 1)]
        for key, val in frequency.items():
            buckets[val].append(key)

        # get k numbers from buckets starting from the end
        output = []
        counted = 0
        for i in range(len(buckets) - 1, -1, -1):
            if counted == k:
                return output
            output += buckets[i]
            counted += len(buckets[i])
        