class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        max_count, count = 0, 0
        left = 0

        for right in range(len(fruits)):
            freq[fruits[right]] += 1
            count += 1

            while len(freq) > 2 and left < len(fruits):
                # pop left most fruit until two types of fruit are remaining
                count -= 1
                freq[fruits[left]] -= 1

                if freq[fruits[left]] == 0:
                    freq.pop(fruits[left])

                left += 1

            max_count = max(max_count, count)

        return max_count